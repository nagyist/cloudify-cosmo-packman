# flake8: NOQA
########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

# from user_definitions import *

# # TODO: add support for "skip_get" and "skip_pack" flags.
# VARIABLES = {
#     "logstash": {

#     },
#     "manager_server_path": "{0}/manager/cloudify-manager-{1}/rest-service/manager_rest/".format(VIRTUALENVS_PATH, MANAGER_BRANCH),
#     "gunicorn_user": "root",
#     "manager_rest_port": "8100",
#     "manager_file_server_dir": "{0}/manager/resources".format(VIRTUALENVS_PATH),
#     "gunicorn_conf_path": "{0}/manager/config/conf/guni.conf".format(VIRTUALENVS_PATH),
#     "unicorn_user": "root",
#     "kibana_run_dir": "/opt/kibana3",
#     "kibana_port": "3000",
#     "nginx_rest_and_ui_port": "80",
#     "nginx_file_server_port": "53229",
#     "nginx_file_server_dir": "{0}/manager/resources".format(VIRTUALENVS_PATH),
#     "rabbitmq_port": "5672",
#     "elasticsearch_port": "9200",
#     "langohr_jar": "{0}/riemann/langohr/langohr.jar".format(COMPONENT_PACKAGES_PATH),
#     "manager_config": "{0}/manager/cloudify-manager-{1}/plugins/riemann-controller/riemann_controller/resources/manager.config".format(VIRTUALENVS_PATH, MANAGER_BRANCH)
#     "celery_init_path": "/etc/init/celeryd-cloudify-management.conf",
#     "celery_run_dir": "{0}/celery".format(VIRTUALENVS_PATH),
#     "ui_log_file": "/var/log/cloudify-ui/cosmo-ui.log",
#     "ui_user": "root",
#     "ui_run_dir": "/opt/cloudify-ui",
#     "ui_port": "9001",
#     "celery_work_dir": "{0}/celery/cloudify.management__worker".format(VIRTUALENVS_PATH),
#     "celery_workers_autoscale": "5,2"
#     "logstash_jar": "logstash.jar",
#     "logstash_log_file": "/var/log/logstash.out",
#     "logstash_conf_path": "/etc/logstash.conf",
#     "logstash_run_dir": "/opt/logstash",
#     "logstash_user": "root",
#     "logstash_events_queue": "cloudify-events",
#     "logstash_logs_queue": "cloudify-logs",
#     "logstash_test_tcp_port": "9999",
#     "logstash_events_index": "cloudify_events",
#     "elasticsearch_run_dir": "/opt/elasticsearch",
#     "elasticsearch_user": "root",
# }
PACKAGES = {
    "logstash": {
        "name": "logstash",
        "version": "1.3.2",
        "get": {
            "source_urls": [ "https://download.elasticsearch.org/logstash/logstash/logstash-1.3.2-flatjar.jar" ],
            "sources_path": "/packages/logstash",
        },
        "pack": {
            "output_types": [
                {
                    "type": "docker_container",
                    "context": {
                        "image": "ubuntu:12.04",
                    },
                },
                {
                    "type": "package",
                    "context": {
                        "formats": ["deb", "rpm"],
                    },
                    "depends": [ "openjdk-7-jdk" ],
                    "package_path": "/test/logstash/",
                }
            ],
            "bootstrap_script": "logstash-bootstrap.sh",
            "bootstrap_template": "logstash-bootstrap.template",
            # "config_templates": {
            #     "template_file_init": {
            #         "template": "{0}/logstash/init/logstash.conf.template".format(CONFIGS_PATH),
            #         "output_file": "logstash.conf",
            #         "config_dir": "config/init",
            #         "dst_dir": "/etc/init",
            #     },
            #     "template_file_conf": {
            #         "template": "{0}/logstash/conf/logstash.conf.template".format(CONFIGS_PATH),
            #         "output_file": "logstash.conf",
            #         "config_dir": "config/conf",
            #         "dst_dir": "/etc",
            #     },
            # }
        },
    },
}