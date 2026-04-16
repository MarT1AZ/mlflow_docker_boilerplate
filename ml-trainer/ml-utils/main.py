import mlflow


tracking_uri = "http://mlflow-server-con:5000"
mlflow.set_tracking_uri(tracking_uri)
mlflow.set_experiment("create inside docker test 2")
print("exitting")