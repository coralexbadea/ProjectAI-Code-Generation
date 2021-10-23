import catalogue
from flask import Blueprint, render_template, request, flash, redirect, url_for
from ..services.nlp.generateCodeService import GenerateCodeService
import json

nlp = Blueprint('nlp', __name__)

generate_code_service = GenerateCodeService()

@nlp.route('/generate_code', methods=['POST'])
def generate_code():
    print(request.get_json())
    string = request.get_json()["string"]
    result = generate_code_service.generateCode(string)[5:]

    return dict(string=result)



