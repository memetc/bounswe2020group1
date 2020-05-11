# routes.py

from flask import Blueprint, abort, jsonify, request
from .models import Comment, Product

bp = Blueprint('routes', __name__, url_prefix='/routes')

@bp.route('</product/int:productId>', methods=['GET'])
def get_product(productId):
    
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

@bp.route('/search/<string:keyword>', methods=['GET'])
def search(keyword):
    if(keyword is not None):
        # TODO autocomplete api   # TODO category instead of name
        product_list = Product.query.filter_by(name = keyword).all()
    else:
        product_list = []
    return jsonify([product.serialize() for product in product_list])
    #return render_template("search.html",product_list=product_list)

@bp.route('/product/<int: productId>/product/', methods=['POST'])
def add_product(productId):
	
    if 'name' not in request.json or 'price' not in request.json or 'location' not in request.json or 'description' not in request.json:
		abort(400)	

    product = Product.create(id=productId,name=request.json['name'], price=request.json['price'],
                             description=request.json['description'], location=request.json['location'])

    return jsonify({'product': product.serialize()})
