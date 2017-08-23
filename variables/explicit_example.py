objects = {
"payment": {
    "funded": "third party", # "recipient", #
    "payment_due_days": 30,
    "late_fee": True,
    "late_fee_percentage": 5,
    "late_fee_timeline": "month",
    "assessor_rate": "$0 USD/hour",
    "externally_funded": True,
    "cancellation_fee": True,
    "assessor_additional_revision_rate": "$0 USD/hour",
    "assessor_provides_additional_service": True,
    "scope_changes_at_recipient_expense": True,
    "predefined_rates_for_additional_work": True,
    "notice_for_changes_to_rates_for_additional_days": True,
    "days_notice_before_rate_change": 15,
    "recipiant_must_pay_for_all_services_upon_termination": True
    },
"privsec": {
    "external_funder": {
        "access": True,
        "information_disclosed": [
            "the number of vulnerabilities identified ",
            "the specific vulnerabilities that are identified",
        ],
        "additional_security": [
            "the Recipient's location, name, and type of work will not be disclosed",
            "the Recipients vulnerabilities will be aggregated with the vulnerabilities of two or more other Recipients the Service Provider is funded to assess.",
            ],
        },
    "confidentiality_term_years": 5,
    "days_for_confidential_notice": 15,
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
        "entity_type": "Colorado 501(c)(3) nonprofit corporation",
        "address": "1600 Pennsylvania Ave NW, Washington, DC 20500",
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
    "service_provider": {
        "name": "ABC Assessing",
        "representative": {
            "name":"Soraya Herce",
            "title": "Principal Consultant",
            },
        "designated_contact": "Maral Mansur",
        "entity_type": "Washington, DC Corporation",
        "address": "1600 Pennsylvania Ave NW, Washington, DC 20500",
        "emergency_contacts": [
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
"disputes": {
    "dispute_resolution_provider": "JAMS",
    "arbitration_earliest_initiation_date": 45,
    "days_adr_tolls_statues_of_limitations": 30,
    "applicable_law": "Washington, DC",
    "days_of_mediation_until_arbitration_forced": 30
    },
"agreement": {
    "termination": {
        "period_of_notice": "30 days",
        "breach_remedy_period": "15 days"
        },
    "date": "July 12th, 2016",
    "term_end": "December 1st, 2016",
    "goal": """The traditional corporate security assessment is based upon an assumption that an organization has the time, money, and manpower to aim for as close to perfect security as possible, and more importantly, that they will be able to have ongoing assessments over time. The Recipient of this assessment has none of these luxuries.

Therefore they have asked the Service Provider to design and use a customized combination of selected assessment techniques derived from standards in the security auditing world to provide a tailored risk assessment and mitigation consultation.

This audit will not only provide an assessment of the Recipients risks, but will also act as a teaching opportunity for the Service Provider to provide the Recipient a map of their digital footprint, an understanding of how their technology is tied to the threats they perceive, and guidance on how to seek out support in the future.

Lastly, the Service Provider is well connected to trusted digital security trainers around the world as well as large networks of resources and broader capabilities, including rapid response networks. They will use these preexisting relationships to help the Recipient identify the support they need to address their vulnerabilities.""",
    "scope_changes_response_days": 15
    },
"deliverables": {
    "includes_report" : True,
    "deliv_items" : [
        "A report that shows the Recipient's current state of security, the process by which the Service Provider came to these conclusions, and recommendations that will guide the Recipient's progression to meet their security goals."],
    "revisions": {
        "number_allowed": 1,
        "minimum_billable_period": "2 hours",
        "days_to_raise_corrections": 15,
        "days_to_fix_deliverable": 15
        },
    "report": {
        "assessment_report_components":"The Recipient's current state of security, the process by which the Service Provider came to these conclusions, and recommendations that will guide the Recipient's progression to meet their security goals",
        "targeting": [
            "The report will contain an easy-to-read executive summary with no technical jargon.",
            "The report will contain sufficient detail that later technical and/or security teams will be able to implement the recommendations.",
            "Each recommendation will include a summary statement that shows proof of need and contains no sensitive information. These statements will be written in a way that will allow the Recipiant to directly copy them into funding proposals."
        ]
        }
    },
"engagement": {
    "activities": [
        {"name": "Assessment preparation",
         "length": "one month",
         "description": "To commence our engagement, Service Provider will meet with IT/Operations leadership for an initial description of the situation and current landscape. Following that session Recipiant will provide Service Provider with any research materials that will be useful to inform Service Provider's knowledge of the organization, its infrastructure, work, and the risks it faces.",
         "begins": "after the signing of the agreement"},
        {"name": "Reconnaissance",
         "length": "the entire length of the assessment",
         "description": "The Service Provider will identify publicly available resources (such as websites, extranets, email servers, but also social media information) connected to the organization and remotely gather information about those resources. It will include both passive reconnaissance of publicly available data sources and active external scans of Recipients network assets.",
         "begins": "alongside assessment preparation"},
        {"name": "Data assessment",
         "length": "throughout the length of the on-site phase",
         "description": "Service Provider will lead staff in activities where they identify where critical data currently resides (what devices/physical locations), who has access (physical, login, permissions), and who needs to have access to do their jobs.",
         "begins": "at the start of the on-site engagement phase"},
        {"name": "Threat assessment",
         "length": "on the first day of the on-site engagement",
         "description": "The Service Provider will carry out a variety of activities to identify possible attackers and gather background information about the capability of those attackers to threaten the Recipients organization. This will include identifying a particular attacker's history of carrying out specific threats, their capability to carry out those threats currently, and intent to expend their resources against the Recipient.",
         "begins": "for two days"},
        {"name": "Report Writing",
         "length": "30 days",
         "description": "The Service Provider will compile their assessment notes and recommendations into a comprehensive set of documents the shows the current state of security, the process by which the Service Provider came to that assessment, and recommendations that will guide Recipient's progression to meet their security goals.",
         "begins": "after all on-site activities have completed"},
        {"name": "Feedback and follow up activities",
         "length": "up to 15 days",
         "description": "The Service Provider will lead a meeting with the primary point of contact to deliver and discuss the reports findings as well as a final follow-up meeting to explain recommendations and answer staff questions.",
         "begins": "upon approval of final report"},],
         "update_meeting_frequency": "once a week"
    },
"pricing": {
    "milestones": [
        {"name": "Remote Assessment",
         "date": "Sept 30th, 2016",
         "price": 20000},
        {"name": "On-Site Assessment",
         "date": "Oct 30th, 2016",
         "price": 20000},
        {"name": "Reporting",
         "date": "Nov 15th, 2016",
         "price": 20000},
        {"name": "Follow Up",
         "date": "December 1st, 2016",
         "price": 20000}
        ],
    "rates": [
        {"name": "Consulting – Principal",
         "comments": "Consulting on strategy and security architecture specification.",
         "hourly_rate": 500},
        {"name": "Consulting - Policy/Practice",
         "comments": "Consulting on security policy and practice development.",
         "hourly_rate": 500},
        {"name": "System Configuration",
         "comments": "Configure networks, systems, and software to respond to identified vulnerabilities",
         "hourly_rate": 500},
        {"name": "Training",
         "comments": "Provide security training's on identified topics",
         "hourly_rate": 500},
         {"name": "Development",
         "comments": "Writing security budgets and grant and proposal language.",
         "hourly_rate": 500}
         ],
    },
"incident_response": {
    "disclosure_period":"1 business day",
    "assessor_mitigate_incident":True,
    "assessor_refer_incident":False,
    "security_incidents_are_force_majeur": True
},
"context": {
    "on_site_activities": True,
}}
