from flask import Flask, request, jsonify
from nameko.standalone.rpc import ClusterRpcProxy

app = Flask(__name__)
CONFIG = {'AMQP_URI': "amqp://guest:guest@localhost"}


@app.route('/heavyprocess', methods=['POST'])
def heavyprocess():
  request_json = request.get_json(force=True)
  process_wm = "Please wait the download, you'll check this endpoint GET - heavyprocess for get results"
  with ClusterRpcProxy(CONFIG) as rpc:
    process = rpc.service_a.dispatching_method.call_async(request_json)
    queue_name = process.reply_event.queue_consumer.queue.name
    return jsonify({'result': process_wm, 'queueName': queue_name}), 200

if __name__ == '__main__':
  app.run(debug=True)