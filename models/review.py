#!/usr/bin/python3

""" module name Revieew inheriting from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class

    inheits from basemodel super class

    """

    place_id = ""
    user_id = ""
    text = ""
