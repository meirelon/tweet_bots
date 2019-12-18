#deploying pickle files to gcs
import pickle
from datetime import datetime
from gcloud import storage
from tempfile import NamedTemporaryFile


def deploy_pickle(object, project_id, bucket, destination_path, filename, local=False):
    client = storage.Client(project=project_id)

    with NamedTemporaryFile(mode='wb') as temp:
        pickle.dump(object, temp)
        temp.seek(0)
        gcs_path = os.path.join(destination_path,
                                '{filename}_{dt}.pkl'.format(filename=filename, dt=datetime.today().strftime("%Y%m%d"))
        client.bucket(bucket).blob(gcs_path).upload_from_filename(temp.name)
