from flask import Flask
from app.controllers.order_controller import order_bp
from app.utils.logger import logger

app = Flask(__name__)

app.register_blueprint(order_bp)

@app.route("/health")
def health():
    return {"status": "UP"}

if __name__ == "__main__":
    logger.info("Starting Order Service...")
    app.run(host="0.0.0.0", port=5000)