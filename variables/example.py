
objects = {
"payment": {
    "client_funded": None,
    "payment_due_days":30,
    "late_fee": 5,
    "late_fee_timeline": "month",
    "assessor_rate": "$0 USD/hour",
    "externally_funded": True,
    },
"privsec": {
    "external_funder": {
        "access": True,
        "information_disclosed": [
            "the number of vulnerabilities identified ",
            "the specific vulnerabilities that are identified",
        ],
        "additional_security": [
            "the recipient's location, name, and type of work will not be disclosed",
            "the recipients vulnerabilities will be aggregated with the vulnerabilities of two or more other recipients the assessor is funded to assess.",
            ],
        },
    "device_security":[
        "all devices will have full-disk encryption enabled and will be powered down when traveling",
        "all mobile devices will have remote wipe enabled",
        "all passwords used on devices will meet or exceed complex password standards",
        "all passwords pertaining to the Recipiants assessment - including, but not limited to Wi-Fi, device\", and service passwords - will be stored in a password manager under an assessment specific \"keering\" and treated as confidential information",
        "all devices will be fully wiped and/or \"factory reset\" upon the completion of the assessment",
        ],
    "data_retention_period": "One Year"
    },
"travel": {
    "expenses": {
        "responsible": "Recipient",
        "payment_conditions": "and will be billed directly to Recipient."
        }
    },
"expenses": {
        "responsible": "Recipient",
        "payment_conditions": "Reimbursable costs must be approved by Recipient in writing in advance of being incurred. Recipient will be invoiced for all reimbursable expenses, together with appropriate documentation evidencing such expenses."
    },
"parties": {
    "recipient": {
        "name": "XYC Company",
        "representative": {
            "name": "Anicetas Švedas",
            "title": "CEO",
            },
        "designated_contact" : "Zou Woei-wan",
        "emergency_contacts": [
            {
                "name":"Gianetta Morbidelli",
                "phone_number":"+353 20 913 XXXX",
                "secure_channel":"pgp: gmorbidel@example.com"
            },
            {
                "name":"Miguel Martínez Buentello",
                "phone_number":"+353 20 139 XXXX",
                "secure_channel":"pgp: mmb2017@example.com",
            },
            {
                "name":"Zou Woei-wan",
                "phone_number":"+353 05 913 XXXX",
                "secure_channel":"Signal: Same Number"
            },
            ]
        },
    "assessor": {
        "name": "ABC Assessing",
        "representative": {
            "name":"Soraya Herce",
            "title": "Principal Consultant",
            },
        "designated_contact" : "Maral Mansur",
        "emergency_contacts":[
            {
                "name":"Maral Mansur",
                "phone_number":"+36 55 754 XXX",
                "secure_channel":"Signal: Same Number"
            },
            {
                "name":"Chun Sang-jin",
                "phone_number":"+36 55 774 XXX",
                "secure_channel":"PGP: ItsAMeSangJin@example.com"
            },
            ]
        }
    },
"agreement": {
    "termination": {
        "period_of_notice": "30 days",
        "breach_remedy_period": "15 days"
        },
    "date": "July 12th, 2016",
    "goal": """The traditional corporate security assessment is based upon an assumption that an organization has the time, money, and manpower to aim for as close to perfect security as possible, and more importantly, that they will be able to have ongoing assessments over time. The recipient of this assessment has none of these luxuries.

Therefore they have asked the assessor to design and use a customized combination of selected assessment techniques derived from standards in the security auditing world to provide a tailored risk assessment and mitigation consultation.

This audit will not only provide an assessment of the recipients risks, but will also act as a teaching opportunity for the assessor to provide the recipient a map of their digital footprint, an understanding of how their technology is tied to the threats they perceive, and guidance on how to seek out support in the future.

Lastly, the assessor is well connected to trusted digital security trainers around the world as well as large networks of resources and broader capabilities, including rapid response networks. They will use these preexisting relationships to help the recipient identify the support they need to address their vulnerabilities."""
    },
"deliverables": {
    "includes_report" : True,
    "deliv_items" : [
        "A report that shows the Recipient's current state of security, the process by which the Assessor came to these conclusions, and recommendations that will guide the Recipient's progression to meet their security goals."],
    "revisions" : {
        "number_allowed": 1,
        "minimum_billable_period": "2 hours",
        "days_to_raise_corrections": 15
        },
    "report": {
        "targeting": [
            "The report will contain an easy-to-read executive summary with no technical jargon.",
            "The report will contain sufficient detail that later technical and/or security teams will be able to implement the recommendations.",
            "Each recommendation will include a summary statement that shows proof of need and contains no sensitive information. These statements will be written in a way that will allow the Recipiant to directly copy them into funding proposals."
        ]
        }
    },
"engagement": {
    "activities": [
        {"name": "assessment preparation phase",
         "length": "one month",
         "begins": "after the signing of the agreement"},
        {"name": "reconnaissance activities",
         "length": "the entire length of the assessment",
         "begins": "alongside assessment preparation"},
        {"name": "data assessment phase",
         "length": "throughout the length of the on-site phase",
         "begins": "at the start of the on-site engagement phase"},
        {"name": "threat assessment",
         "length": "on the first day of the on-site engagement",
         "begins": "for two days"},
        {"name": "deliverables will be produced and provided to the client, in accordance with the deliverables section, during the reporting phase. This",
         "length": "30 days",
         "begins": "after all on-site activities have completed"},
        {"name": "feedback and follow up activities",
         "length": "up to 15 days",
         "begins": "once the Recipiant approves of the final report"},],
   "update_meeting_frequency": "once a week"
    },
"incident_response": {
    "disclosure_period":"1 business day",
    "assessor_mitigate_incident":True,
    "assessor_refer_incident":False,
},
"context": {
    "on_site_activities": True,
}}
