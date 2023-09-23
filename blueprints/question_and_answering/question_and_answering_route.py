from flask import Blueprint, jsonify, request
from decouple import config
from haystack.document_stores import PineconeDocumentStore
from haystack.nodes import EmbeddingRetriever
from haystack.pipelines import GenerativeQAPipeline
from haystack.nodes import Seq2SeqGenerator

from errors import handle_internal_server_error, handle_not_processable_error

question_and_answering_bp = Blueprint("query", __name__)

API_KEY = config("DOC_STORE_API_KEY")
DOC_STORE_ENV = config("DOC_STORE_ENV")


document_store = PineconeDocumentStore(
    api_key=API_KEY,
    index="vital-ai",
    similarity="cosine",
    embedding_dim=768,
    environment=DOC_STORE_ENV,
)

retriever = EmbeddingRetriever(
    document_store=document_store,
    embedding_model="flax-sentence-embeddings/all_datasets_v3_mpnet-base",
    model_format="sentence_transformers",
)


generator = Seq2SeqGenerator(model_name_or_path="vblagoje/bart_lfqa")


pipe = GenerativeQAPipeline(generator, retriever)


@question_and_answering_bp.route("/query-answer", methods=["POST"])
def question_and_answering_fn():
    data = request.get_json()
    if not data["query"]:
        return handle_not_processable_error("")
    user_query = data["query"]
    try:
        result = pipe.run(
            query=user_query,
            params={"Retriever": {"top_k": 3}, "Generator": {"top_k": 1}},
        )["answers"][0].answer
        return jsonify({"result": result})
    except Exception as e:
        print(e)
        return handle_internal_server_error("")
