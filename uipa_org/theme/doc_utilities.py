#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2016 Ryan Kanno <ryankanno@localkinegrinds.com>
#
# Distributed under terms of the MIT license.

import datetime
from docx import Document
import os
from uipa_org.uipa_constants import (FOOTER_DELIMITER,
                                     WELCOME_DELIMITER,
                                     WAIVER_DELIMITER)


def is_requesting_waiver(text):
    '''
    Return True if requestor enters anything below the delimiter in the Your
    Request field on the Request form.
    '''
    parts = text.split(WAIVER_DELIMITER)
    if len(parts) < 2:
        return False
    return len(parts[1].strip()) > 0


def _strip_contents_after(phrase, lines):
    '''Returns lines before the line that contains the phrase'''
    if not phrase:
        return lines

    start = 0
    for (i, line) in enumerate(lines):
        if line.find(phrase) > -1:
            start = i

    return lines[:start]


def prepare_for_description(text):
    ''' Returns text without everything after waiver delimiter'''
    lines = text.split('\r\n')
    lns = _strip_contents_after(WAIVER_DELIMITER, lines)
    return '\r\n'.join(lns)


def prepare_for_pdf(text):
    ''' Returns the text with only the text body,
        and waiver request, but no delimiter and footer'''
    parts = text.split(WELCOME_DELIMITER)

    if len(parts) == 2:
        rest_of_request_form = parts[1].strip()
        request_form_parts = rest_of_request_form.split(FOOTER_DELIMITER)
        if len(request_form_parts) == 2:
            request_form = request_form_parts[0].strip()
            lines = request_form.split('\r\n')
            lns = [line for line in lines if line.find(WAIVER_DELIMITER) == -1]
            return '\r\n'.join(lns)

        raise Exception("Unable to find the FOOTER_DELIMITER while preparing for pdf")

    raise Exception("Unable to find the WELCOME_DELIMITER while preparing for pdf")


def prepare_for_final_archiving(text):
    ''' Returns the text with everything except for the waiver request '''
    parts = text.split(WAIVER_DELIMITER)

    if len(parts) == 2:
        waiver_to_end = parts[1].strip()
        waiver_parts = waiver_to_end.split(FOOTER_DELIMITER)
        if len(waiver_parts) == 2:
            return "{0}{1}{2}".format(
                parts[0], FOOTER_DELIMITER, waiver_parts[1])

        raise Exception("Unable to find the FOOTER_DELIMITER while preparing for final archiving")

    raise Exception("Unable to find the WELCOME_DELIMITER while preparing for final archiving")


def create_uipa_document_request_from_foi_request(foi_request, should_waive_fees):
    curr = os.path.dirname(os.path.realpath(__file__))
    return create_uipa_document_request(
        os.path.join(curr, 'data/Request-Access-form-12.1.15-fillable.docx'),
        datetime.datetime.utcnow(),
        foi_request.public_body.name,
        foi_request.public_body.email,
        foi_request.secret_address,
        foi_request.secret_address,
        foi_request.secret_address,
        prepare_for_pdf(foi_request.messages[0].plaintext),
        should_waive_fees)


def create_uipa_document_request(
    document_path,
    request_date,
    agency_name,
    agency_contact_information,
    requester_name,
    requester_contact_information,
    requester_email_address,
    request_text,
    should_waive_fees):

    # TODO: @ryankanno - Make case insensitive regexs at some point
    DELIMITER_REPLACEMENT_MAP = {
        "[Request_Date]": request_date.strftime('%m-%d-%Y'),
        "[Agency_Name]": agency_name,
        "[Agency_Contact_Information]": agency_contact_information,
        "[Requester_Name]": requester_name,
        "[Requester_Contact_Information]": requester_contact_information,
        "[Requester_Email_Address]": requester_email_address,
        "[Request]": request_text
    }

    document = Document(document_path)
    paragraphs = document.paragraphs

    for idx, paragraph in enumerate(paragraphs):
        for k, v in list(DELIMITER_REPLACEMENT_MAP.items()):
            if k in paragraph.text:
                paragraph.text = paragraph.text.replace(k, v)

        if "[CB]" in paragraph.text:
            paragraph.text = paragraph.text.replace(
                "[CB]",
                "[X]" if should_waive_fees else "[ ]")

    return document


if __name__ == "__main__":
    """
    Testing, yo.
    """
    fee_wavier = False
    document = create_uipa_document_request(
        './data/Request-Access-form-12.1.15-fillable.docx',
        datetime.datetime.utcnow(),
        "Department of Development",
        "Ryan Kanno",
        "Sara Kanno",
        "sara@kanno.io",
        "sara@kanno.io",
        "Can I get access to code?",
        fee_wavier)

    document.save(
        './data/{0}-FALSE-Request-Access-form-12.1.15-fillable.docx'.format(
            datetime.datetime.utcnow().isoformat()))

    fee_wavier = True
    body = "Can I get access to code?\r\n\r\n%s\r\nBecause, it's public." % WAIVER_DELIMITER
    stripped_body = strip_for_request(body)

    document = create_uipa_document_request(
        './data/Request-Access-form-12.1.15-fillable.docx',
        datetime.datetime.utcnow(),
        "Department of Development",
        "Ryan Kanno",
        "Sara Kanno",
        "sara@kanno.io",
        "sara@kanno.io",
        stripped_body,
        fee_wavier)

    document.save(
        './data/{0}-TRUE-Request-Access-form-12.1.15-fillable.docx'.format(
            datetime.datetime.utcnow().isoformat()))

# vim: fenc=utf-8
# vim: filetype=python
