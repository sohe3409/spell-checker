""" Module for errors """

class SearchMiss(Exception):
    """class for index exceptions"""
    def __str__(self):
        """Error message"""
        return "The word was not spelled correctly"
