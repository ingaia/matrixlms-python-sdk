import matrixsdk.http

SUPPORTED_CALLS = [
	'get_version',
	'get_my_account',
	'get_all_users',
	'get_users_with_ids',
	'get_users_that_match',
	'add_user',
	'get_all_classes',
	'get_classes_with_ids',
	'get_classes_that_match',
	'get_classes_for_organization',
	'get_classes_taught_by',
	'get_classes_enrolled_by',
	'get_teachers_for_class',
	'get_students_for_class',
	'add_students_to_class',
	'remove_students_from_class',
	'get_all_organizations',
	'get_organizations_with_ids',
	'get_all_certificates',
	'get_certificates_with_ids',
	'get_lessons_for_class',
	'get_assignments_for_class'
]

class APIError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)


class API(object):
	"""Programmatic Interface to Matrix LMS API

	Supported Calls:
	get_version()
	get_my_account()
	get_all_users()
	get_users_with_ids(user_ids)  
	get_users_that_match(constraints)
	add_user(attributes)
	get_all_classes()
	get_classes_with_ids(class_ids) 
	get_classes_that_match(constraints)
	get_classes_for_organization(organization_id) 
	get_classes_taught_by(user_id)
	get_classes_enrolled_by(user_id) 
	get_teachers_for_class(class_id) 
	get_students_for_class(class_id)  
	add_students_to_class(class_id, user_ids)  
	remove_students_from_class(class_id, user_ids)  
	get_all_organizations()  
	get_organizations_with_ids(organization_ids)  
	get_all_certificates() 
	get_certificates_with_ids(certificate_ids) 
	get_lessons_for_class(class_id)   
	get_assignments_for_class(class_id)

	Doctests:
	Get all users
    >>> API().get_all_users()['status_code']
    200

    Try to call a non supported service
    >>> API().method_not_supported()
    Traceback (most recent call last):
     ...   	
    APIError: 'Method not supported.'
	"""

	HOST = 'gaia360.matrixlms.com'
	API_KEY = '12048-445151-2d3ef76f4782582f3b68aad0544ff2f15dc083cc'	
	USE_SSL = False

	def __getattr__(self, method):
		if method in SUPPORTED_CALLS:
			def function(*args):
				protocol = 'https' if self.USE_SSL else 'http'	
				endpoint = '%s://%s/api/%s' % (protocol, self.HOST, method)
				params = args[0] if len(args) > 0 else {}
				params['api_key'] = self.API_KEY
				return matrixsdk.http.execute_get(endpoint, params)
			return function
		else:
			raise APIError('Method not supported.')