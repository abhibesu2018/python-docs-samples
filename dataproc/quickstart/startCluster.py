import sys
sys.path.append('/home/abhi/eclipse-welcome/python-docs-samples/dataproc')
from dataproc.create_cluster import create_cluster
if __name__=="__main__":
    import os
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/abhi/Downloads/dataproc-273223-f4f81b36b7e5.json'
    project_id = 'dataproc-273223'
    cluster_name = 'sparkjobs'
    region = 'australia-southeast1'

    create_cluster(project_id, region, cluster_name, timeout=30)