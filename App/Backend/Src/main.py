# Copyright 2025 Dagim 
#
# Licensed under the Apache License, Version 2.0 (the "License");

import sqlite3
from datetime import date

from initentity import InitEntity
from db_connection import initalize_database
from Slipher_io import * # Because Slipher_io is used to process user input there is no need to specify each function name.

from subject import Subject
from topic import Topic
from config import db_path, schema_file


def main():
    """Main program loop."""
    initalize_database(db_path, schema_file)

    subject_handler = Subject(db_path)
    topic_handler = Topic(db_path)

    while True:
        print("\nOptions:")
        print("1. Add Subjects")
        print("2. Add Topics")
        print("3. Edit Subject")
        print("4. Edit Topic")
        print("5. Delete Subject")
        print("6. Delete Topic")
        print("7. Exit")

        choice = input("Choose an option:\n> ").strip()

        if choice == "1":
            add_subjects(subject_handler)
        elif choice == "2":
            add_topics(topic_handler)
        elif choice == "3":
            edit_subject(subject_handler)
        elif choice == "4":
            edit_topic(topic_handler)
        elif choice == "5":
            delete_subject(subject_handler)
        elif choice == "6":
            delete_topic(topic_handler)
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose again.")

