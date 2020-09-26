from nawah.classes import APP_CONFIG, ATTR, PACKAGE_CONFIG
from nawah.enums import NAWAH_VALUES

config = APP_CONFIG(
    name='my_awesome_blog',
    version='0.1.0',
    # Use this App Config Attr to determine which env to use based on value of environment variable ENV
    env='$__env.ENV',
    envs={
        'dev_local': PACKAGE_CONFIG(
            debug=True, data_server='mongodb://localhost'
        ),
        'dev_server': PACKAGE_CONFIG(
            debug=True,
            # Use this Config Attr to emulate test mode. Read more on Test Workflow on Nawah Docs.
            # emulate_test=True,
            data_server='mongodb://admin:admin@mongodb',
            # Use this Config Attr to determine port on which app is served based on value of environment variable PORT. Any Config Attr can be set at root level
            # port='$__env.PORT',
            # You can use data_name Config Attr for custom data_name per env
            # data_name='nawah_data'
        ),
        'prod': PACKAGE_CONFIG(
            # Use this App Config Attr to set debug mode based on existence of environment variable DEBUG
            # debug='$__env.DEBUG',
            data_server='mongodb://admin:admin@prod',
            # Use this App Config Attr to force use of SSL connection
            data_ssl=True,
        ),
    },
    # define name of the database for your app
    data_name='nawah_data',
    # Define app locales in the form of language_COUNTRY
    locales=['ar_AE', 'en_AE'],
    # Define app default locale, which is the required value for LOCALE Attr Type
    locale='ar_AE',
    # Define user attrs, these are unique attributes per user that can be used to authenticate the user
    user_attrs={
        'email': ATTR.EMAIL(),
        # 'username': ATTR.STR(),
        # 'phone': ATTR.PHONE(),
    },
    # Define user_settings, these are user-specific settings that are created with Setting module, in order to give access to users to these settings without breaching User module security model
    # user_settings={
    # 	# If you define a user_settings item with type: user, it means user has ability to change its value using setting/update call
    # 	# If you define a user_settings item with default: NAWAH_VALUES.NONE_VALUE, it means this settings attr requires a value at time of creating user. Notice that we had to supply a value for ADMIN doc to avoid breaking Nawah app launch
    # 	'age': {
    # 		'type': 'user',
    # 		'val_type': ATTR.INT(ranges=[[18, 121]]),
    # 		'default': NAWAH_VALUES.NONE_VALUE,
    # 	},
    # 	# If you would like to have a default value so that if user/create call doesn't fail for not specifying a value, you can set a matching default value
    # 	'bio': {
    # 		'type': 'user',
    # 		'val_type': ATTR.LOCALE(),
    # 		'default': {'ar_AE': None},
    # 	},
    # 	# If you define a user_settings item with type: user_sys, it means this settings attr is available for the user to read but not update
    # 	# For, this type settings attr, a default value HAS TO BE provided and it would be used, where any supplied value in user/create doc would be ignored for this settings attr
    # 	'points': {
    # 		'type': 'user_sys',
    # 		'val_type': ATTR.INT(),
    # 		'default': 0,
    # 	},
    # },
    # Specify which of user_settings to be appended to User doc at time of reading it. This means attrs in the list would be present for all docs in user/read call results. Notice, 'age' is missing--To get User 'age' settings attr, setting/read call can be used
    # user_doc_settings=['bio', 'points'],
    # Set ADMIN doc values. This is the default ADMIN doc value that will be created to allow you to authenticate and manage the data
    admin_doc={
        'email': 'admin@app.nawah.localhost',
        # '...':'...'
    },
    # Define ADMIN password that will be used to generate the hashes
    admin_password='Rg!2/U$~]M/h!F>REW',
    # Define ANON token. This token is used as salt across Nawah framework so it is very good idea to change it from default token
    anon_token='__ANON_TOKEN_307880618201630497643197',
    # Define default privileges any authenticated user is having. Usually it's suggested all users have file: create, setting: update, privileges as they are basic access requirements to any app, however, if you create proxy modules where you would like to have more control over these privileges you can always drop the default privileges
    default_privileges={
        'file': ['create'],
        'setting': ['update'],
        # 'module_name': ['privilege1', 'privilege2', ..., 'privilege0'],
    }
    # Learn more about Config Attrs on Nawah Docs.
)
