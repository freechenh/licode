#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: big_file.py
# @Author: dell
# @Date: 2021/1/4  16:32
# @Desc: 
# @Project: licode
# @Source: PyCharm


data = r"""
2021-01-04 16:38:26  INFO mylog.py log_i [ line:178 ] [conftest.py->common_function->18]-[start test case]:test_templates_create_008>>>>>>>>>>>>>>测试用例执行开始>>>>>>>>>>>>>>
2021-01-04 16:38:26  INFO mylog.py log_i [ line:178 ] [templates.py->get_protocol_info->40]->>>>>>>>>>>>>>存储协议额外参数>>>>>>>>>>>>>>
2021-01-04 16:38:26  INFO mylog.py log_i [ line:178 ] [rpc_interface.py->exchange->50]-<<<<<<<<<<<request url https://172.28.100.159:9260/v1/password/template_writer
2021-01-04 16:38:26  INFO mylog.py log_i [ line:178 ] [rpc_interface.py->exchange->51]-<<<<<<<<<<<request data None
2021-01-04 16:38:26  INFO mylog.py log_i [ line:178 ] [rpc_interface.py->exchange->52]-<<<<<<<<<<<request action None
2021-01-04 16:38:26  INFO mylog.py log_i [ line:178 ] [rpc_interface.py->exchange->69]-<<<<<<<<<<<<<<<response data {'code': 0, 'message': None, 'user_tip': None, 'data': {'user': 'template_writer', 'password': 'ZDQXZYzU5MjAz'}}
2021-01-04 16:38:26  INFO mylog.py log_i [ line:178 ] [templates.py->openapi_templates_create->76]->>>>>>>>>>>>>>1.创建模板接口>>>>>>>>>>>>>>
2021-01-04 16:38:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__post_do->124]---->http request post :https://172.28.100.159:9250/rccp/rest/v1/compute/templates
2021-01-04 16:38:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__post_do->126]-data:{'content': {'template_id': None, 'template_name': 'test_2021-01-04_16_38_26_1', 'template_desc': '默认模板1', 'storage_pool_id': '00000000-0000-0000-0000-000000000000', 'cluster_id': 'f9bb5975-52e9-4f4f-aa8f-1640bbbbd69f', 'size': 62, 'fileInfoReq': {'relative_path': 'RCDC_Pro_Win7_64_V004.qcow2', 'protocol_type': 'SAMBA', 'protocol_options': {'username': 'template_writer', 'password': 'ZDQXZYzU5MjAz', 'share_name': 'template', 'server_name': '172.28.100.159', 'port': 445}}}}
2021-01-04 16:38:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__post_do->137]-<---response 200
2021-01-04 16:38:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__post_do->139]-{'content': {'code': 0, 'data': {'template_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e'}}}
2021-01-04 16:38:26  INFO mylog.py _commonlib_log_i [ line:230 ] [common_assert.py->common_assert_equal->48]-test_templates_create_008:  assert true
2021-01-04 16:38:26  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:27  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:28  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:29  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:30  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:31  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:32  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:33  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:34  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:36  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:37  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:38  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:39  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:40  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:41  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:42  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:43  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:44  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:45  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:46  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:47  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:48  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:49  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:50  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:51  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:52  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:54  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:55  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:56  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:57  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:58  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:38:59  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:38:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:38:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:38:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:38:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:00  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:01  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:02  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:03  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:04  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:05  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:06  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:07  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:08  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:09  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:10  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:11  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:13  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:14  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:15  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:16  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:17  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:18  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:19  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:20  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:21  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:22  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:23  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:24  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:25  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:26  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:27  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:28  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:29  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:30  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:32  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:33  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:34  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:35  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:36  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:37  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:38  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:39  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:40  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:41  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:42  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:43  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:44  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:45  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:46  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:47  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:48  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:50  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:51  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:52  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:53  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:54  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:55  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:56  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:57  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:58  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:39:59  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:39:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:39:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:39:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:39:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:00  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:01  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:02  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:03  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:04  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:05  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:06  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:08  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:09  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:10  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:11  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:12  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:13  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:14  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:15  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:16  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:17  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:18  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:19  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:20  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:21  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:22  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:23  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:24  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:25  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:27  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:28  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:29  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:30  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:31  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:32  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:33  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:34  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:35  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:36  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:37  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:38  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:39  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:40  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:41  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:42  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:43  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:44  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:46  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:47  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:48  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:49  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:50  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:51  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:52  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:53  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:54  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:55  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:56  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:57  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:58  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:40:59  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:40:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:40:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:40:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:40:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:00  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:01  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:02  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:04  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:05  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:06  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:07  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:08  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:09  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:10  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:11  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:12  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:13  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:14  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:15  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:16  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:17  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:18  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:19  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:20  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:22  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:23  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:24  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:25  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:26  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:27  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:28  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:29  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:30  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:31  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:32  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:33  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:34  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:35  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:36  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:37  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:38  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:39  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:41  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:42  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:43  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:44  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:45  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:46  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:47  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:48  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:49  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'FINISHED'}], 'total': 1}}}
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [task.py->wait_task_finish->81]-<<<<<<<<<<CREATE任务完成
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->231]-cost_count:204.3849537372589
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->238]-创建模板接口耗时：204.3849537372589
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->239]-创建模板平均时长为：204.3849537372589
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->240]-创建模板最大时长为：204.3849537372589
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->241]-创建模板最小时长为：204.3849537372589
2021-01-04 16:41:50  INFO mylog.py _commonlib_log_i [ line:230 ] [common_assert.py->common_assert_equal->48]-test_templates_create_008:  assert true
2021-01-04 16:41:50  INFO mylog.py _commonlib_log_i [ line:230 ] [common_assert.py->common_assert_equal->48]-test_templates_create_008:  assert true
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->246]-<Response [200]>
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [templates.py->get_protocol_info->40]->>>>>>>>>>>>>>存储协议额外参数>>>>>>>>>>>>>>
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [rpc_interface.py->exchange->50]-<<<<<<<<<<<request url https://172.28.100.159:9260/v1/password/template_writer
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [rpc_interface.py->exchange->51]-<<<<<<<<<<<request data None
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [rpc_interface.py->exchange->52]-<<<<<<<<<<<request action None
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [rpc_interface.py->exchange->69]-<<<<<<<<<<<<<<<response data {'code': 0, 'message': None, 'user_tip': None, 'data': {'user': 'template_writer', 'password': 'ZDQXZYzU5MjAz'}}
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [templates.py->openapi_templates_create->76]->>>>>>>>>>>>>>1.创建模板接口>>>>>>>>>>>>>>
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__post_do->124]---->http request post :https://172.28.100.159:9250/rccp/rest/v1/compute/templates
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__post_do->126]-data:{'content': {'template_id': None, 'template_name': 'test_2021-01-04_16_41_50_2', 'template_desc': '默认模板2', 'storage_pool_id': '00000000-0000-0000-0000-000000000000', 'cluster_id': 'f9bb5975-52e9-4f4f-aa8f-1640bbbbd69f', 'size': 62, 'fileInfoReq': {'relative_path': 'RCDC_Pro_Win7_64_V004.qcow2', 'protocol_type': 'SAMBA', 'protocol_options': {'username': 'template_writer', 'password': 'ZDQXZYzU5MjAz', 'share_name': 'template', 'server_name': '172.28.100.159', 'port': 445}}}}
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__post_do->137]-<---response 200
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__post_do->139]-{'content': {'code': 0, 'data': {'template_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377'}}}
2021-01-04 16:41:50  INFO mylog.py _commonlib_log_i [ line:230 ] [common_assert.py->common_assert_equal->48]-test_templates_create_008:  assert true
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:51  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:53  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:54  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:55  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:56  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:57  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:58  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:41:59  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:41:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:41:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:41:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:41:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:00  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:01  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:02  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:03  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:04  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:05  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:06  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:07  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:08  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:09  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:11  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:12  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:13  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:14  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:15  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:16  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:17  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:18  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:19  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:20  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:21  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:22  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:23  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:24  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:25  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:26  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:27  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:28  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:30  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:31  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:32  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:33  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:34  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:35  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:36  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:37  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:38  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:39  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:40  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:41  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:42  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:43  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:44  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:45  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:46  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:48  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:49  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:50  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:51  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:52  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:53  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:54  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:55  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:56  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:57  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:58  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:42:59  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:42:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:42:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:42:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:42:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:00  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:01  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:02  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:03  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:04  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:05  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:07  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:08  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:09  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:10  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:11  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:12  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:13  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:14  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:15  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:16  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:17  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:18  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:19  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:20  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:21  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:22  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:23  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:24  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:26  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:27  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:28  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:29  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:30  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:31  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:32  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:33  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:34  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:35  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:36  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:37  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:38  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:39  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:40  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:41  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:42  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:44  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:45  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:46  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:47  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:48  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:49  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:50  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:51  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:52  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:53  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:54  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:55  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:56  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:57  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:58  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:43:59  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:43:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:43:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:43:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:43:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:00  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:01  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:03  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:04  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:05  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:06  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:07  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:08  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:09  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:10  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:11  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:12  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:13  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:14  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:15  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:16  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:17  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:18  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:19  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:21  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:22  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:23  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:24  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:25  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:26  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:27  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:28  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:29  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:30  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:31  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:32  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:33  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:34  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:35  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:36  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:37  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:38  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:40  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:41  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:42  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:43  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:44  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:45  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:46  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:47  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:48  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:49  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:50  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:51  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:52  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:53  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:54  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:55  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:56  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:58  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:44:59  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:44:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:44:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:44:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:44:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:00  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:01  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:02  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:03  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:04  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:05  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:06  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:07  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:08  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:09  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:10  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:11  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:12  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:13  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:14  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:15  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'FINISHED'}], 'total': 1}}}
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [task.py->wait_task_finish->81]-<<<<<<<<<<CREATE任务完成
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->231]-cost_count:206.44974493980408
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->238]-创建模板接口耗时：206.44974493980408
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->239]-创建模板平均时长为：206.44974493980408
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->240]-创建模板最大时长为：206.44974493980408
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->241]-创建模板最小时长为：206.44974493980408
2021-01-04 16:45:17  INFO mylog.py _commonlib_log_i [ line:230 ] [common_assert.py->common_assert_equal->48]-test_templates_create_008:  assert true
2021-01-04 16:45:17  INFO mylog.py _commonlib_log_i [ line:230 ] [common_assert.py->common_assert_equal->48]-test_templates_create_008:  assert true
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->246]-<Response [200]>
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [templates.py->get_protocol_info->40]->>>>>>>>>>>>>>存储协议额外参数>>>>>>>>>>>>>>
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [rpc_interface.py->exchange->50]-<<<<<<<<<<<request url https://172.28.100.159:9260/v1/password/template_writer
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [rpc_interface.py->exchange->51]-<<<<<<<<<<<request data None
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [rpc_interface.py->exchange->52]-<<<<<<<<<<<request action None
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [rpc_interface.py->exchange->69]-<<<<<<<<<<<<<<<response data {'code': 0, 'message': None, 'user_tip': None, 'data': {'user': 'template_writer', 'password': 'ZDQXZYzU5MjAz'}}
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [templates.py->openapi_templates_create->76]->>>>>>>>>>>>>>1.创建模板接口>>>>>>>>>>>>>>
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__post_do->124]---->http request post :https://172.28.100.159:9250/rccp/rest/v1/compute/templates
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__post_do->126]-data:{'content': {'template_id': None, 'template_name': 'test_2021-01-04_16_45_17_3', 'template_desc': '默认模板3', 'storage_pool_id': '00000000-0000-0000-0000-000000000000', 'cluster_id': 'f9bb5975-52e9-4f4f-aa8f-1640bbbbd69f', 'size': 62, 'fileInfoReq': {'relative_path': 'RCDC_Pro_Win7_64_V004.qcow2', 'protocol_type': 'SAMBA', 'protocol_options': {'username': 'template_writer', 'password': 'ZDQXZYzU5MjAz', 'share_name': 'template', 'server_name': '172.28.100.159', 'port': 445}}}}
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__post_do->137]-<---response 200
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__post_do->139]-{'content': {'code': 0, 'data': {'template_id': 'b5f655b0-bd63-4432-bea1-174aacde1093'}}}
2021-01-04 16:45:17  INFO mylog.py _commonlib_log_i [ line:230 ] [common_assert.py->common_assert_equal->48]-test_templates_create_008:  assert true
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:18  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:19  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:20  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:21  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:22  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:23  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:24  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:25  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:26  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:27  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:28  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:30  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:31  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:32  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:33  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:34  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:35  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:36  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:37  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:38  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:39  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:40  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:41  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:42  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:43  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:44  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:45  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:46  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:47  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:49  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:50  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:51  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:52  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:53  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:54  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:55  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:56  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:57  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:58  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:45:59  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:45:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:45:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:45:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:45:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:00  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:01  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:02  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:03  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:04  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:05  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:07  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:08  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:09  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:10  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:11  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:12  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:13  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:14  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:15  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:16  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:17  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:18  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:19  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:20  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:21  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:22  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:23  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:24  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:26  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:27  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:28  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:29  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:30  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:31  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:32  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:33  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:34  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:35  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:36  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:37  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:38  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:39  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:40  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:41  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:42  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:44  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:45  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:46  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:47  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:48  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:49  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:50  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:51  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:52  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:53  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:54  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:55  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:56  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:57  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:58  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:46:59  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:46:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:46:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:46:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:46:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:00  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:02  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:03  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:04  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:05  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:06  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:07  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:08  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:09  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:10  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:11  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:12  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:13  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:14  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:15  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:16  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:17  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:18  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:20  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:21  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:22  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:23  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:24  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:25  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:26  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:27  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:28  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:29  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:30  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:31  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:32  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:33  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:34  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:35  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:36  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:37  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:39  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:40  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:41  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:42  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:43  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:44  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:45  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:46  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:47  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:48  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:49  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:50  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:51  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:52  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:53  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:54  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:55  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:57  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:58  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:47:59  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:47:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:47:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:47:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:47:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:00  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:01  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:02  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:03  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:04  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:05  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:06  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:07  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:08  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:09  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:10  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:11  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:12  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:13  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:14  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:16  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:17  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:18  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:19  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:20  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:21  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:22  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:23  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:24  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:25  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:26  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:27  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:28  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:29  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:30  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:31  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:32  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:34  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:35  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:36  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:37  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:38  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'FINISHED'}], 'total': 1}}}
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [task.py->wait_task_finish->81]-<<<<<<<<<<CREATE任务完成
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->231]-cost_count:202.2699716091156
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->238]-创建模板接口耗时：202.2699716091156
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->239]-创建模板平均时长为：202.2699716091156
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->240]-创建模板最大时长为：202.2699716091156
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->241]-创建模板最小时长为：202.2699716091156
2021-01-04 16:48:39  INFO mylog.py _commonlib_log_i [ line:230 ] [common_assert.py->common_assert_equal->48]-test_templates_create_008:  assert true
2021-01-04 16:48:39  INFO mylog.py _commonlib_log_i [ line:230 ] [common_assert.py->common_assert_equal->48]-test_templates_create_008:  assert true
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->246]-<Response [200]>
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [templates.py->get_protocol_info->40]->>>>>>>>>>>>>>存储协议额外参数>>>>>>>>>>>>>>
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [rpc_interface.py->exchange->50]-<<<<<<<<<<<request url https://172.28.100.159:9260/v1/password/template_writer
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [rpc_interface.py->exchange->51]-<<<<<<<<<<<request data None
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [rpc_interface.py->exchange->52]-<<<<<<<<<<<request action None
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [rpc_interface.py->exchange->69]-<<<<<<<<<<<<<<<response data {'code': 0, 'message': None, 'user_tip': None, 'data': {'user': 'template_writer', 'password': 'ZDQXZYzU5MjAz'}}
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [templates.py->openapi_templates_create->76]->>>>>>>>>>>>>>1.创建模板接口>>>>>>>>>>>>>>
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__post_do->124]---->http request post :https://172.28.100.159:9250/rccp/rest/v1/compute/templates
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__post_do->126]-data:{'content': {'template_id': None, 'template_name': 'test_2021-01-04_16_48_39_4', 'template_desc': '默认模板4', 'storage_pool_id': '00000000-0000-0000-0000-000000000000', 'cluster_id': 'f9bb5975-52e9-4f4f-aa8f-1640bbbbd69f', 'size': 62, 'fileInfoReq': {'relative_path': 'RCDC_Pro_Win7_64_V004.qcow2', 'protocol_type': 'SAMBA', 'protocol_options': {'username': 'template_writer', 'password': 'ZDQXZYzU5MjAz', 'share_name': 'template', 'server_name': '172.28.100.159', 'port': 445}}}}
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__post_do->137]-<---response 200
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__post_do->139]-{'content': {'code': 0, 'data': {'template_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d'}}}
2021-01-04 16:48:39  INFO mylog.py _commonlib_log_i [ line:230 ] [common_assert.py->common_assert_equal->48]-test_templates_create_008:  assert true
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:40  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:41  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:42  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:43  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:44  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:45  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:47  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:48  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:49  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:50  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:51  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:52  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:53  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:54  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:55  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:56  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:57  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:58  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:48:59  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:48:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:48:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:48:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:48:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:00  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:01  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:02  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:03  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:05  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:06  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:07  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:08  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:09  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:10  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:11  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:12  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:13  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:14  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:15  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:16  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:17  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:18  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:19  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:20  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:21  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:22  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:24  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:25  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:26  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:27  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:28  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:29  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:30  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:31  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:32  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:33  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:34  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:35  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:36  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:37  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:38  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:39  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:40  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:41  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:43  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:44  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:45  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:46  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:47  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:48  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:49  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:50  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:51  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:52  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:53  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:54  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:55  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:56  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:57  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:58  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:49:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:49:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:49:59  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:49:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:49:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:01  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:02  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:03  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:04  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:05  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:06  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:07  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:08  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:09  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:10  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:11  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:12  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:13  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:14  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:15  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:16  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:17  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:19  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:20  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:21  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:22  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:23  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:24  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:25  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:26  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:27  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:28  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:29  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:30  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:31  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:32  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:33  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:34  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:35  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:36  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:38  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:39  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:40  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:41  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:42  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:43  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:44  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:45  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:46  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:47  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:48  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:49  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:50  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:51  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:52  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:53  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:54  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:56  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:57  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:58  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:50:59  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:50:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:50:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:50:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:50:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:00  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:01  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:02  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:03  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:04  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:05  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:06  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:07  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:08  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:09  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:10  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:11  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:12  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:13  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:15  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:16  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:17  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:18  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:19  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:20  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:21  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:22  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:23  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:24  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:25  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:26  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:27  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:28  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:29  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:30  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:31  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:33  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:34  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:35  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:36  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:37  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:38  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:39  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:40  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:41  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:42  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:43  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:44  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:45  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:46  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:47  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:48  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:49  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:50  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:52  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:53  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:54  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:55  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:56  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:57  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:58  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:51:59  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:51:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:51:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:51:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:51:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:00  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'FINISHED'}], 'total': 1}}}
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [task.py->wait_task_finish->81]-<<<<<<<<<<CREATE任务完成
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->231]-cost_count:202.24302530288696
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->238]-创建模板接口耗时：202.24302530288696
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->239]-创建模板平均时长为：202.24302530288696
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->240]-创建模板最大时长为：202.24302530288696
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->241]-创建模板最小时长为：202.24302530288696
2021-01-04 16:52:01  INFO mylog.py _commonlib_log_i [ line:230 ] [common_assert.py->common_assert_equal->48]-test_templates_create_008:  assert true
2021-01-04 16:52:01  INFO mylog.py _commonlib_log_i [ line:230 ] [common_assert.py->common_assert_equal->48]-test_templates_create_008:  assert true
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->246]-<Response [200]>
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [templates.py->get_protocol_info->40]->>>>>>>>>>>>>>存储协议额外参数>>>>>>>>>>>>>>
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [rpc_interface.py->exchange->50]-<<<<<<<<<<<request url https://172.28.100.159:9260/v1/password/template_writer
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [rpc_interface.py->exchange->51]-<<<<<<<<<<<request data None
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [rpc_interface.py->exchange->52]-<<<<<<<<<<<request action None
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [rpc_interface.py->exchange->69]-<<<<<<<<<<<<<<<response data {'code': 0, 'message': None, 'user_tip': None, 'data': {'user': 'template_writer', 'password': 'ZDQXZYzU5MjAz'}}
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [templates.py->openapi_templates_create->76]->>>>>>>>>>>>>>1.创建模板接口>>>>>>>>>>>>>>
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__post_do->124]---->http request post :https://172.28.100.159:9250/rccp/rest/v1/compute/templates
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__post_do->126]-data:{'content': {'template_id': None, 'template_name': 'test_2021-01-04_16_52_01_5', 'template_desc': '默认模板5', 'storage_pool_id': '00000000-0000-0000-0000-000000000000', 'cluster_id': 'f9bb5975-52e9-4f4f-aa8f-1640bbbbd69f', 'size': 62, 'fileInfoReq': {'relative_path': 'RCDC_Pro_Win7_64_V004.qcow2', 'protocol_type': 'SAMBA', 'protocol_options': {'username': 'template_writer', 'password': 'ZDQXZYzU5MjAz', 'share_name': 'template', 'server_name': '172.28.100.159', 'port': 445}}}}
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__post_do->137]-<---response 200
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__post_do->139]-{'content': {'code': 0, 'data': {'template_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d'}}}
2021-01-04 16:52:01  INFO mylog.py _commonlib_log_i [ line:230 ] [common_assert.py->common_assert_equal->48]-test_templates_create_008:  assert true
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:02  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:03  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:05  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:06  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:07  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:08  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:09  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:10  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:11  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:12  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:13  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:14  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:15  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:16  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:17  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:18  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:19  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:20  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:21  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:23  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:24  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:25  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:26  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:27  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:28  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:29  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:30  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:31  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:32  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:33  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:34  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:35  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:36  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:37  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:38  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:39  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:40  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:42  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:43  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:44  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:45  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:46  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:47  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:48  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:49  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:50  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:51  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:52  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:53  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:54  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:55  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:56  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:57  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:58  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:52:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:52:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:52:59  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:52:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:52:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:01  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:02  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:03  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:04  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:05  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:06  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:07  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:08  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:09  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:10  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:11  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:12  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:13  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:14  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:15  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:16  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:17  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:19  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:20  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:21  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:22  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:23  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:24  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:25  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:26  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:27  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:28  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:29  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:30  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:31  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:32  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:33  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:34  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:35  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:36  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:38  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:39  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:40  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:41  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:42  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:43  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:44  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:45  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:46  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:47  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:48  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:49  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:50  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:51  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:52  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:53  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:54  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:56  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:57  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:58  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:53:59  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:53:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:53:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:53:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:53:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:00  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:01  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:02  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:03  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:04  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:05  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:06  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:07  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:08  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:09  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:10  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:11  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:12  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:14  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:15  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:16  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:17  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:18  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:19  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:20  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:21  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:22  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:23  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:24  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:25  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:26  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:27  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:28  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:29  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:30  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:31  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:33  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:34  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:35  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:36  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:37  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:38  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:39  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:40  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:41  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:42  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:43  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:44  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:45  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:46  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:47  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:48  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:49  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:51  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:52  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:53  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:54  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:55  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:56  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:57  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:58  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:54:59  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:54:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:54:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:54:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:54:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:00  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:00  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:01  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:01  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:02  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:02  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:03  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:03  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:04  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:04  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:05  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:05  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:06  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:06  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:07  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:07  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:08  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:09  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:09  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:10  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:10  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:11  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:11  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:12  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:12  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:13  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:13  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:14  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:14  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:15  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:15  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:16  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:16  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:17  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:17  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:18  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:18  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:19  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:19  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:20  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:20  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:21  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:21  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:22  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:22  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:23  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:23  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:24  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:24  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:25  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:25  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:26  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:26  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:27  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'CREATE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'CREATE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'FINISHED'}], 'total': 1}}}
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [task.py->wait_task_finish->81]-<<<<<<<<<<CREATE任务完成
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->231]-cost_count:206.51196026802063
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->238]-创建模板接口耗时：206.51196026802063
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->239]-创建模板平均时长为：206.51196026802063
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->240]-创建模板最大时长为：206.51196026802063
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->241]-创建模板最小时长为：206.51196026802063
2021-01-04 16:55:28  INFO mylog.py _commonlib_log_i [ line:230 ] [common_assert.py->common_assert_equal->48]-test_templates_create_008:  assert true
2021-01-04 16:55:28  INFO mylog.py _commonlib_log_i [ line:230 ] [common_assert.py->common_assert_equal->48]-test_templates_create_008:  assert true
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [test_templates_create.py->test_templates_create_008->246]-<Response [200]>
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [templates.py->openapi_templates_list_get->101]->>>>>>>>>>>>>>3.查询模板列表接口>>>>>>>>>>>>>>
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__get_do->73]---->http request get :https://172.28.100.159:9250/rccp/rest/v1/compute/templates?page=0&limit=1000
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__get_do->75]-data:None
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__get_do->77]-<---response 200
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__get_do->79]-{'content': {'code': 0, 'data': {'items': [{'capacity': 42949672960, 'cluster_id': 'f9bb5975-52e9-4f4f-aa8f-1640bbbbd69f', 'create_time': 1609750321070, 'last_update_time': 1609750526872, 'storage_pool_id': '00000000-0000-0000-0000-000000000000', 'template_desc': '默认模板5', 'template_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'template_name': 'test_2021-01-04_16_52_01_5', 'template_status': 'NORMAL'}, {'capacity': 42949672960, 'cluster_id': 'f9bb5975-52e9-4f4f-aa8f-1640bbbbd69f', 'create_time': 1609750118824, 'last_update_time': 1609750320537, 'storage_pool_id': '00000000-0000-0000-0000-000000000000', 'template_desc': '默认模板4', 'template_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'template_name': 'test_2021-01-04_16_48_39_4', 'template_status': 'NORMAL'}, {'capacity': 42949672960, 'cluster_id': 'f9bb5975-52e9-4f4f-aa8f-1640bbbbd69f', 'create_time': 1609749916546, 'last_update_time': 1609750118063, 'storage_pool_id': '00000000-0000-0000-0000-000000000000', 'template_desc': '默认模板3', 'template_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'template_name': 'test_2021-01-04_16_45_17_3', 'template_status': 'NORMAL'}, {'capacity': 42949672960, 'cluster_id': 'f9bb5975-52e9-4f4f-aa8f-1640bbbbd69f', 'create_time': 1609749710118, 'last_update_time': 1609749915882, 'storage_pool_id': '00000000-0000-0000-0000-000000000000', 'template_desc': '默认模板2', 'template_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'template_name': 'test_2021-01-04_16_41_50_2', 'template_status': 'NORMAL'}, {'capacity': 42949672960, 'cluster_id': 'f9bb5975-52e9-4f4f-aa8f-1640bbbbd69f', 'create_time': 1609749505702, 'last_update_time': 1609749709616, 'storage_pool_id': '00000000-0000-0000-0000-000000000000', 'template_desc': '默认模板1', 'template_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'template_name': 'test_2021-01-04_16_38_26_1', 'template_status': 'NORMAL'}, {'capacity': 42949672960, 'cluster_id': 'f9bb5975-52e9-4f4f-aa8f-1640bbbbd69f', 'create_time': 1609746269617, 'last_update_time': 1609747457484, 'storage_pool_id': '00000000-0000-0000-0000-000000000000', 'template_desc': '默认模板', 'template_id': '410f2c4a-b415-4a15-902e-4fb5b942b83e', 'template_name': 'auto_create_template', 'template_status': 'NORMAL'}, {'capacity': 64424509440, 'cluster_id': 'f9bb5975-52e9-4f4f-aa8f-1640bbbbd69f', 'create_time': 1609736917749, 'last_update_time': 1609737185571, 'storage_pool_id': '00000000-0000-0000-0000-000000000000', 'template_id': 'a1ae0fd6-4825-4c0a-b682-1220a0a193a1', 'template_name': 'a1ae0fd648254c0ab6821220a0a193a1', 'template_status': 'NORMAL'}, {'capacity': 64424509440, 'cluster_id': 'f9bb5975-52e9-4f4f-aa8f-1640bbbbd69f', 'create_time': 1609736272955, 'last_update_time': 1609736531177, 'storage_pool_id': '00000000-0000-0000-0000-000000000000', 'template_id': '45845556-9004-41de-9070-4bc3f2aa7370', 'template_name': '45845556900441de90704bc3f2aa7370', 'template_status': 'NORMAL'}, {'capacity': 64424509440, 'cluster_id': 'f9bb5975-52e9-4f4f-aa8f-1640bbbbd69f', 'create_time': 1609735664989, 'last_update_time': 1609736961524, 'storage_pool_id': '00000000-0000-0000-0000-000000000000', 'template_id': '3fc0d6f5-b4e8-4f30-86eb-57402c93a1bc', 'template_name': '3fc0d6f5b4e84f3086eb57402c93a1bc', 'template_status': 'NORMAL'}, {'capacity': 1073741824, 'cluster_id': 'f9bb5975-52e9-4f4f-aa8f-1640bbbbd69f', 'create_time': 1609731657579, 'last_update_time': 1609731668453, 'storage_pool_id': '00000000-0000-0000-0000-000000000000', 'template_id': '989e8f9f-4d46-42c6-bdde-2d1723b1951c', 'template_name': '1609731596956_personalCfg.qcow2', 'template_status': 'NORMAL'}, {'capacity': 5368709120, 'cluster_id': 'f9bb5975-52e9-4f4f-aa8f-1640bbbbd69f', 'create_time': 1609731598807, 'last_update_time': 1609731618131, 'storage_pool_id': '00000000-0000-0000-0000-000000000000', 'template_id': '74c34b5e-6e82-4b58-a42a-087fb742c492', 'template_name': '1609731596956_layer.qcow2', 'template_status': 'NORMAL'}, {'capacity': 1073741824, 'cluster_id': 'f9bb5975-52e9-4f4f-aa8f-1640bbbbd69f', 'create_time': 1609731598443, 'last_update_time': 1609731618141, 'storage_pool_id': '00000000-0000-0000-0000-000000000000', 'template_id': 'eed5b7be-9978-4ba8-aa4b-2c4fc2a1311c', 'template_name': '1609731596956_personal.qcow2', 'template_status': 'NORMAL'}], 'total': 12}}}
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [templates.py->openapi_templates_delete_interface->85]->>>>>>>>>>>>>>2.删除模板接口>>>>>>>>>>>>>>
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__delete_do->234]---->http request delete :https://172.28.100.159:9250/rccp/rest/v1/compute/templates/fe10f75d-71b2-415e-80bd-90f78fdae14d
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__delete_do->241]-<---response 200
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__delete_do->243]-{'content': {'code': 0}}
2021-01-04 16:55:28  INFO mylog.py _commonlib_log_i [ line:230 ] [common_assert.py->common_assert_equal->48]-:  assert true
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:28  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:29  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:29  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:30  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:30  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:31  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:31  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:32  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:32  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:33  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:33  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:34  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:34  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:35  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:35  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:36  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'fe10f75d-71b2-415e-80bd-90f78fdae14d', 'run_state': 'FINISHED'}], 'total': 1}}}
2021-01-04 16:55:36  INFO mylog.py log_i [ line:178 ] [task.py->wait_task_finish->81]-<<<<<<<<<<DELETE任务完成
2021-01-04 16:55:36  INFO mylog.py log_i [ line:178 ] [templates.py->openapi_templates_delete_interface->85]->>>>>>>>>>>>>>2.删除模板接口>>>>>>>>>>>>>>
2021-01-04 16:55:36  INFO mylog.py log_i [ line:178 ] [http_interface.py->__delete_do->234]---->http request delete :https://172.28.100.159:9250/rccp/rest/v1/compute/templates/07978c6e-3f4c-45ce-9d8b-8dc745bd490d
2021-01-04 16:55:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__delete_do->241]-<---response 200
2021-01-04 16:55:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__delete_do->243]-{'content': {'code': 0}}
2021-01-04 16:55:37  INFO mylog.py _commonlib_log_i [ line:230 ] [common_assert.py->common_assert_equal->48]-:  assert true
2021-01-04 16:55:37  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:37  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:38  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:38  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:39  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:39  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:40  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:40  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:41  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:41  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:42  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': '07978c6e-3f4c-45ce-9d8b-8dc745bd490d', 'run_state': 'FINISHED'}], 'total': 1}}}
2021-01-04 16:55:42  INFO mylog.py log_i [ line:178 ] [task.py->wait_task_finish->81]-<<<<<<<<<<DELETE任务完成
2021-01-04 16:55:42  INFO mylog.py log_i [ line:178 ] [templates.py->openapi_templates_delete_interface->85]->>>>>>>>>>>>>>2.删除模板接口>>>>>>>>>>>>>>
2021-01-04 16:55:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__delete_do->234]---->http request delete :https://172.28.100.159:9250/rccp/rest/v1/compute/templates/b5f655b0-bd63-4432-bea1-174aacde1093
2021-01-04 16:55:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__delete_do->241]-<---response 200
2021-01-04 16:55:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__delete_do->243]-{'content': {'code': 0}}
2021-01-04 16:55:42  INFO mylog.py _commonlib_log_i [ line:230 ] [common_assert.py->common_assert_equal->48]-:  assert true
2021-01-04 16:55:42  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:42  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:43  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:43  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:44  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:44  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:45  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:45  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:46  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:46  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:47  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:47  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'b5f655b0-bd63-4432-bea1-174aacde1093', 'run_state': 'FINISHED'}], 'total': 1}}}
2021-01-04 16:55:47  INFO mylog.py log_i [ line:178 ] [task.py->wait_task_finish->81]-<<<<<<<<<<DELETE任务完成
2021-01-04 16:55:48  INFO mylog.py log_i [ line:178 ] [templates.py->openapi_templates_delete_interface->85]->>>>>>>>>>>>>>2.删除模板接口>>>>>>>>>>>>>>
2021-01-04 16:55:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__delete_do->234]---->http request delete :https://172.28.100.159:9250/rccp/rest/v1/compute/templates/f6aed74c-5f6d-44f1-9eb1-e3f021c1f377
2021-01-04 16:55:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__delete_do->241]-<---response 200
2021-01-04 16:55:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__delete_do->243]-{'content': {'code': 0}}
2021-01-04 16:55:48  INFO mylog.py _commonlib_log_i [ line:230 ] [common_assert.py->common_assert_equal->48]-:  assert true
2021-01-04 16:55:48  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:48  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:49  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:49  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:50  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:50  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:51  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:51  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:52  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:52  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:53  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'f6aed74c-5f6d-44f1-9eb1-e3f021c1f377', 'run_state': 'FINISHED'}], 'total': 1}}}
2021-01-04 16:55:53  INFO mylog.py log_i [ line:178 ] [task.py->wait_task_finish->81]-<<<<<<<<<<DELETE任务完成
2021-01-04 16:55:53  INFO mylog.py log_i [ line:178 ] [templates.py->openapi_templates_delete_interface->85]->>>>>>>>>>>>>>2.删除模板接口>>>>>>>>>>>>>>
2021-01-04 16:55:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__delete_do->234]---->http request delete :https://172.28.100.159:9250/rccp/rest/v1/compute/templates/e9cd2818-8909-4a4d-9b91-3edbffda1f0e
2021-01-04 16:55:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__delete_do->241]-<---response 200
2021-01-04 16:55:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__delete_do->243]-{'content': {'code': 0}}
2021-01-04 16:55:53  INFO mylog.py _commonlib_log_i [ line:230 ] [common_assert.py->common_assert_equal->48]-:  assert true
2021-01-04 16:55:53  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:53  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:54  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:54  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:55  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:55  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:56  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:56  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:57  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:57  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'RUNNING'}], 'total': 1}}}
2021-01-04 16:55:58  INFO mylog.py log_i [ line:178 ] [task.py->openapi_task_get->56]->>>>>>>>>>>>>>查询任务执行情况接口>>>>>>>>>>>>>>
2021-01-04 16:55:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->183]---->http request put :https://172.28.100.159:9250/rccp/rest/v1/tasks/action
2021-01-04 16:55:58  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->185]-data:{'content': {'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'limit': 1, 'operate_type': 'DELETE', 'resource_type': 'TEMPLATE'}}
2021-01-04 16:55:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->190]-<---response 200
2021-01-04 16:55:59  INFO mylog.py log_i [ line:178 ] [http_interface.py->__put_do->192]-{'content': {'code': 0, 'data': {'items': [{'operate_type': 'DELETE', 'resource_id': 'e9cd2818-8909-4a4d-9b91-3edbffda1f0e', 'run_state': 'FINISHED'}], 'total': 1}}}
2021-01-04 16:55:59  INFO mylog.py log_i [ line:178 ] [task.py->wait_task_finish->81]-<<<<<<<<<<DELETE任务完成
2021-01-04 16:55:59  INFO mylog.py log_i [ line:178 ] [conftest.py->common_function->20]-[end test case]:test_templates_create_008>>>>>>>>>>>>>>测试用例执行结束>>>>>>>>>>>>>>"""

with open('./xxx.txt', 'wb') as f:
    f.write(data.encode())
