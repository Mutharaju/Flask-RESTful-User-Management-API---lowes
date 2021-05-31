from flask_restful import Resource

class About(Resource):
    def get(self):
        return {'About Developer':{ 'name':"Mutharaju H M",
                                    'experience':'3.3 year',
                                    'mobile':'9663958234',
                                    'primary skills': [
                                                            "Core Python",
                                                            "Frameworks - Django,Flask",
                                                            "ORMs - sqlalchemy",
                                                            "RESTful APIs - Flask-RESTful",
                                                            "Understanding multi-process architecture",
                                                            'Docker and Container',
                                                            "Agile Development",
                                                            "Central Repository (Git/Bitbucket)"
                                                            ],
                                    'secondary skills': [
                                       " CI / CD pipeline",
                                        "DevOps Culture",
                                        "Linux Commands and Shell Script",
                                        "Angular 5 & 6",
                                        "HTML5, CSS3, JavaScript",
                                        "Bootstrap Framework",
                                        "C, C + + and Core Java"

                                    ],
                         }
                }
