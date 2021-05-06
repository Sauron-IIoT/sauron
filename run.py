from app.repository.camera import capture
from app.repository.context_broker import get_product, create_product

capture_id = capture()

print(f'captured picture: ./captures/{capture_id}.jpg')

product_id = create_product({
    'type': "product",
    'name': {
        'type': 'string',
        'value': 'screw'
    }
})

product = get_product(product_id)

print(f'product created: {product}')
