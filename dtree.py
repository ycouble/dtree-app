#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import fire


SPEC_JSON = "spec.json"

class Question:
    def __init__(self, name, spec):
        self.name = name
        for kw, val in spec.items():
            if kw in ["reponses", "branches"]:
                continue
            setattr(self, kw, val)
        if self.type != "end":
            # Création des réponses
            self.reponses = Answers(self.type, spec["reponses"])
            # Création des branches
            self.branches = [Question(name, branch) for name, branch in spec["branches"].items()]

    def ask(self):
        print(self)

    def __repr__(self):
        return f"[[{self.name}]] " + (self.question if self.question else "Fin du questionnaire")

    def show(self, prefix=""):
        print(f"{prefix}{self}")
        print(f"{prefix}({self.description})")
        if self.type != "end":
            print(f"{prefix}Réponses:")
            self.reponses.show(prefix)
            print(f"{prefix}Branches:")
            for branch in self.branches:
                branch.show(prefix="--"+prefix)


class Option:
    def __init__(self, name, desc):
        self.name = name
        self.dest = desc.pop("dest")
        self.params = desc

    def __repr__(self):
        return f"{self.name} --> {self.dest}"


class Answers:
    def __init__(self, type_, options):
        self.type = type_
        self.options = [Option(name, desc) for name, desc in options.items()]

    def show(self, prefix=""):
        for opt in self.options:
            print(f"{prefix} - {opt}")


def show_questionnaire(json_spec_path=SPEC_JSON):
    with open(json_spec_path, "r") as json_spec:
        questionnaire = json.load(json_spec)
    name, content = list(questionnaire.items())[0]
    first_question = Question(name, content)
    first_question.show()


if __name__ == "__main__":
    fire.Fire(show_questionnaire)


