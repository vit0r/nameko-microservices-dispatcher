from flask import Flask, jsonify, request
from nameko.standalone.rpc import ClusterRpcProxy

app = Flask(__name__)
CONFIG = {"AMQP_URI": "amqp://guest:guest@localhost"}


@app.route("/heavyprocess", methods=["POST"])
def heavyprocess():
    request_json = request.get_json(force=True)
    process_wm = "Please wait the download, you'll check this endpoint GET - queue/:queueName for get results"
    with ClusterRpcProxy(CONFIG) as rpc:
        process = rpc.service_a.post_message.call_async(request_json)
        queue_name = str(process.reply_event.queue_consumer.queue.name).strip()
        return jsonify({"result": process_wm, "queueName": queue_name}), 200


@app.route("/queue/<string:queue_name>", methods=["GET"])
def get_message_queue_name(queue_name):
    with ClusterRpcProxy(CONFIG) as rpc:
        result_message = rpc.service_a.get_message.call_async(queue_name)
        print(result_message)
        if result_message:
            return (
                jsonify(
                    {"resultMessage": result_message.result(), "queueName": queue_name}
                ),
                200,
            )
        return jsonify({}), 204


if __name__ == "__main__":
    app.run(debug=True)
