# -*- coding: utf-8 -*-

"""Copyright Header Details

Copyright
---------
    Copyright (C) Guya , PLC - All Rights Reserved (As Of Pending...)
    Unauthorized copying of this file, via any medium is strictly prohibited
    Proprietary and confidential

LICENSE
-------
    This file is subject to the terms and conditions defined in
    file 'LICENSE.txt', which is part of this source code package.

Authors
-------
    * [Simon Belete](https://github.com/Simonbelete)
 
Project
-------
    * Name: 
        - Guya E-commerce & Guya Express
    * Sub Project Name:
        - Profanity Detector
    * Description
        - English and Amharic profanity detector
"""


"""This module registers the error handler on the application."""


from flask import jsonify
from werkzeug.exceptions import HTTPException, default_exceptions


def register_handler(app) -> None:
    """Registers the error handler is a function to common error HTTP codes

    Parameters:
    ----------
        app (flask.app.Flask): The application instance.
    """

    ################################################################
    #
    # generic error handlers
    #
    ################################################################

    # http codes generic error handler
    def generic_http_error_handler(error):
        """Deal with HTTP exceptions.

        Parameters:
        ----------
            error (HTTPException): A werkzeug.exceptions.BadRequest exception object.

        Returns:
        -------
            A flask response object.
        """
        if isinstance(error, HTTPException):
            result = {
                'status_code': error.code,
                'status': error.description,
                'message': "Flask Http Exception",
                'error': {
                    'message': str(error),
                    'type': 'HTTPException'
                }}
        else:
            result = {
                'status_code': 500,
                'status': 'Internal Server Error',
                'message': "Flask Http Exception",
                'error': {
                    'message': str(error),
                    'type': 'Exception'
                }}

        log_exception(error = error, extra = result)
        resp = jsonify(result)
        resp.status_code = result['status_code']
        return resp

    # register http code errors
    for code in default_exceptions.keys():
        app.register_error_handler(code, generic_http_error_handler)
