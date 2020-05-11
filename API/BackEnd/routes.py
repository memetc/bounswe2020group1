# routes.py

from flask import Blueprint, abort, jsonify, request
from .models import Comment, Product

bp = Blueprint('routes', __name__, url_prefix='/routes')

@bp.route('</product/int:productId>', methods=['GET'])
def get_predictions(productId):
    
	prod = Product.query.filter_by(id=productId).first()

	if pred is None:
		return jsonify([])
	else:
		return jsonify(pred.serialize())


@bp.route('/product/<int: productId>/comment/', methods=['POST'])
def add_comment(productId):
	
	if 'author' not in request.json or 'commentText' not in request.json:
		abort(400)
    
	comment = Comment.create(author=request.json['author'], productId=productId, commentText=request.json['commentText'])

	return jsonify({'comment': comment.serialize()})
