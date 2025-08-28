import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.chatbot import build_rag_chain

@pytest.fixture(scope="module")
def rag_chain():
    # Setup: build the RAG chain once for all tests
    return build_rag_chain()

def test_rag_chain_builds(rag_chain):
    assert rag_chain is not None, "RAG chain should be created"

def test_rag_chain_responds(rag_chain):
    question = "What is DrivePK?"
    response = rag_chain.invoke({"input": question})
    assert "answer" in response, "Response should contain an 'answer'"
    assert response["answer"] != "", "Answer should not be empty"
