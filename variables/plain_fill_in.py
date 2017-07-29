objects = {
"payment": {
    "client_funded": True,
    "payment_due_days": "{{DAYS UNTIL PAYMENT DUE}}",
    "late_fee_percentage": "{{LATE FEE PERCENTAGE}}",
    "late_fee_timeline": "{{PERIOD UNTIL DUE}}",
    "assessor_rate": "{{ASSESSORS DAILY/HOURLY RATE}}",
    "externally_funded": None,
    },
"travel": {
    "expenses": {
        "responsible": "{{RESPONSIBLE PARTY}}",
        "payment_conditions": "{{TRAVEL EXPENSE REIMBURSEMENT CONDITIONS}}"
        }
    },
"expenses": {
        "responsible": "{{RESPONSIBLE PARTY}}",
        "payment_conditions": "{{EXPENSE REIMBURSEMENT CONDITIONS}}"
    },
"parties": {
    "recipient": {
        "name": "{{RECIPIENT NAME}}",
        "representative": {
            "name": "{{RECIPIENT REPRESENTATIVE NAME}}",
            "title": "{{RECIPIENT REPRESENTATIVE TITLE}}"
            },
        "designated_contact" : "{{RECIPTIENT DESIGNATED CONTACT}}",
        "emergency_contacts":[
            {
                "name":"{{CONTACT NAME}}",
                "phone_number":"{{CONTACT NUMBER}}",
                "secure_channel":"{{CONTACT SECURE CONTACT}}"
            },
            {
                "name":"{{CONTACT NAME}}",
                "phone_number":"{{CONTACT NUMBER}}",
                "secure_channel":"{{CONTACT SECURE CONTACT}}"
            },
            {
                "name":"{{CONTACT NAME}}",
                "phone_number":"{{CONTACT NUMBER}}",
                "secure_channel":"{{CONTACT SECURE CONTACT}}"
            }
            ]
        },
        "assessor": {
            "name": "{{ASSESSOR NAME}}",
            "representative": {
                "name": "{{ASSESSOR REPRESENTATIVE NAME}}",
                "title": "{{ASSESSOR REPRESENTATIVE TITLE}}"
                },
            "designated_contact" : "{{ASSESSOR DESIGNATED CONTACT}}",
            },
        "emergency_contacts":[
            {
                "name":"{{CONTACT NAME}}",
                "phone_number":"{{CONTACT NUMBER}}",
                "secure_channel":"{{CONTACT SECURE CONTACT}}"
            },
            {
                "name":"{{CONTACT NAME}}",
                "phone_number":"{{CONTACT NUMBER}}",
                "secure_channel":"{{CONTACT SECURE CONTACT}}"
            },
            {
                "name":"{{CONTACT NAME}}",
                "phone_number":"{{CONTACT NUMBER}}",
                "secure_channel":"{{CONTACT SECURE CONTACT}}"
            },
            ]
    },
"agreement": {
    "termination": {
        "period_of_notice": "{{PERIOD OF NOTICE NEEDED FOR TERMINATION}}",
        "breach_remedy_period": "{{PERIOD FOR BREACH TO BE REMEDIED}}"
        },
    "date": "{{DATE CONTRACT TAKES FORCE}}",
    "goal": "{{BEFORE WRITING YOUR AGREEMENT, DECIDE WHAT YOUR GOALS ARE FOR THE CONTRACT. EVERY ASSESSMENT SHOULD BE GOAL-ORIENTED. INSERT WHAT YOUR GOAL IS HERE. A GOOD LEGAL CONTRACT IS ONE THAT CAPTURES THE INTENTIONS OF THE PARTIES ACCURATELY.}}"
    },
"deliverables": {
    "report" : True,
    "deliv_items" : [
        "A report that shows the Recipient's current state of security, the process by which the Assessor came to these conclusions, and recommendations that will guide the Recipient's progression to meet their security goals.",
        "{{ADDITIONAL DELIVERABLES}}",
        "{{ADDITIONAL DELIVERABLES}}",
        "{{ADDITIONAL DELIVERABLES}}",
        "{{ADDITIONAL DELIVERABLES}}"
        ],
        "revisions" : {
            "number_allowed": "{{NUMBER OF REVISIONS}}",
            "minimum_billable_period": "{{MINIMUM DAYS/HOURS}}",
            "days_to_raise_corrections": "{{NUMBER OF BUSINESS DAYS}}"
            },
        "report": {
            "targeting": [
                "{{A way the report is tailored.}}",
                "{{i.e. The report will contain an easy-to-read executive summary with no technical jargon.}}",
                "{{i.e. The report will contain sufficient detail that later technical and/or security teams will be able to implement the recommendations.}}",
                "{{ i.e. Each recommendation will include a summary statement that shows proof of need and contains no sensitive information. These statements will be written in a way that will allow the Recipiant to directly copy them into funding proposals.}}",
                "{{ i.e. Each recommendation will include a summary statement that shows proof of need and contains no sensitive information. These statements will be written in a way that will allow the Recipiant to directly copy them into funding proposals.}}"
                ],
            }
    },
"engagement": {
    "activities": [
        {"name": "{{ACTIVITY WITHIN THE ENGAGEMENT}}",
         "length": "{{LENGTH OF TIME ACTIVITY WILL TAKE}}",
         "begins": "{{WHEN THIS BEGINS}}"},
        {"name": "{{ACTIVITY WITHIN THE ENGAGEMENT}}",
         "length": "{{LENGTH OF TIME ACTIVITY WILL TAKE}}",
         "begins": "{{WHEN THIS BEGINS}}"},
        {"name": "{{ACTIVITY WITHIN THE ENGAGEMENT}}",
         "length": "{{LENGTH OF TIME ACTIVITY WILL TAKE}}",
         "begins": "{{WHEN THIS BEGINS}}"},
        {"name": "{{ACTIVITY WITHIN THE ENGAGEMENT}}",
         "length": "{{LENGTH OF TIME ACTIVITY WILL TAKE}}",
         "begins": "{{WHEN THIS BEGINS}}"},
        {"name": "{{ACTIVITY WITHIN THE ENGAGEMENT}}",
         "length": "{{LENGTH OF TIME ACTIVITY WILL TAKE}}",
         "begins": "{{WHEN THIS BEGINS}}"},],
    "update_meeting_frequency": "{{MEETING FREQUENCY}}",
    },
"incident_response": {
    "disclosure_period":"{{INCIDENT DISCLOSURE PERIOD}}",
    "assessor_mitigate_incident":True,
    "assessor_refer_incident":False,
},
"privsec": {
    "external_funder": {
        "access": True,
        "information_disclosed": [
            "{{Agreed upon piece of information}}",
            "{{Agreed upon piece of information}}",
            "{{Agreed upon piece of information}}",
            "{{Agreed upon piece of information}}",
        ],
        "additional_security": [
            "{{Data sanitation, aggregation, and/or security practice}}",
            "{{Data sanitation, aggregation, and/or security practice}}",
            "{{Data sanitation, aggregation, and/or security practice}}",
            "{{Data sanitation, aggregation, and/or security practice}}",
            ],
        },
        "device_security": [
            "{{DEVICE SECURITY PRACTICE}}",
            "{{DEVICE SECURITY PRACTICE}}",
            "{{DEVICE SECURITY PRACTICE}}",
            ],
    "data_retention_period": "{{DATA RETENTION PERIOD}}",
    },
"context": {
    "on_site_activities": True,
}}
