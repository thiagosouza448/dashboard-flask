#!/usr/bin/python3

import jenkins

jc = jenkins.Jenkins('http://192.168.0.200:8080')



# # print(jc.get_version())
# jc.create_job('4521 - Exemplo', jenkins.EMPTY_CONFIG_XML)

# queue = jc.build_job('Pipeline')

# for job in jc.get_jobs():
# 	print(job ['name'])


# xml = jc.get_job_config('Job')

# print(xml)

# with open('job.xml','r') as xml:
# 	jc.reconfig_job('job', xml.read())

jc.build_job('Job')