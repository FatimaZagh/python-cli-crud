import click
from app.crud import add_product, list_products, get_product, update_product, delete_product, reset_products

@click.group()
def cli():
    pass

@cli.command()
def list():
    products = list_products()
    if not products:
        click.echo("No products found")
    else:
        click.echo("ID | Name | Price")
        for p in products:
            click.echo(f"{p['id']} | {p['name']} | {p['price']}")

@cli.command()
@click.argument("name")
@click.argument("price", type=float)
def add(name, price):
    product = add_product(name, price)
    click.echo(f"Added {product['name']} with price {product['price']}")

@cli.command()
@click.argument("product_id", type=int)
def get(product_id):
    product = get_product(product_id)
    if product:
        click.echo(f"{product['id']} | {product['name']} | {product['price']}")
    else:
        click.echo("Product not found")

@cli.command()
@click.argument("product_id", type=int)
@click.argument("name")
@click.argument("price", type=float)
def update(product_id, name, price):
    product = update_product(product_id, name, price)
    if product:
        click.echo(f"Updated: {product['id']} | {product['name']} | {product['price']}")
    else:
        click.echo("Product not found")

@cli.command()
@click.argument("product_id", type=int)
def delete(product_id):
    if delete_product(product_id):
        click.echo(f"Product {product_id} deleted")
    else:
        click.echo("Product not found")

@cli.command()
def reset():
    reset_products()
    click.echo("All products removed and IDs reset")

if __name__ == "__main__":
    cli()