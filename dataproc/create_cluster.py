#!/usr/bin/env python

# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This sample walks a user through creating a Cloud Dataproc cluster using
# the Python client library.

# [START dataproc_create_cluster]
from google.cloud import dataproc_v1 as dataproc


def create_cluster(project_id, region, cluster_name,**kwargs):
    """This sample walks a user through creating a Cloud Dataproc cluster
       using the Python client library.

       Args:
           project_id (string): Project to use for creating resources.
           region (string): Region where the resources should live.
           cluster_name (string): Name to use for creating a cluster.
    """

    # Create a client with the endpoint set to the desired cluster region.
    cluster_client = dataproc.ClusterControllerClient(client_options={
        'api_endpoint': '{}-dataproc.googleapis.com:443'.format(region)
    })

    # Create the cluster config.
    cluster= {
            "project_id": project_id,
            "cluster_name": cluster_name,
            "config": {
                "config_bucket": "abhi-dataproc-logs",
                "gce_cluster_config": {
                    "zone_uri": "australia-southeast1-b",
                    "metadata": {
                        "meta_key": "meta_value"
                    }
                },
                "master_config": {
                    "num_instances": 1,
                    "machine_type_uri": "n1-standard-1",
                    "disk_config": {
                        "boot_disk_type": "pd-standard",
                        "boot_disk_size_gb": 15,
                        "num_local_ssds": 0
                    },
                    "accelerators": []
                },
                "worker_config": {
                    "num_instances": 2,
                    "machine_type_uri": "n1-standard-2",
                    "disk_config": {
                        "boot_disk_type": "pd-standard",
                        "boot_disk_size_gb": 15,
                        "num_local_ssds": 0
                    },
                    "accelerators": []
                },
                "software_config": {
                    "image_version": "1.4-ubuntu18",
                    "properties": {},
                    "optional_components": []
                },
                "secondary_worker_config": {
                    "num_instances": 0,
                    "is_preemptible": True
                },
                "initialization_actions": [
                    {
                        "executable_file": "gs://abhi-dataproc-logs/init/init.sh"
                    }
                ]
            },
         }

    # Create the cluster.
    operation = cluster_client.create_cluster(project_id, region, cluster,timeout=kwargs['timeout'])
    result = operation.result()

    # Output a success message.
    print('Cluster created successfully: {}'.format(result.cluster_name))
    # [END dataproc_create_cluster]
