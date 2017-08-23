# Safetag Agreement Generator

An assessment agreement generator using Jinja2 templates. Takes a user provided meta-data // assessment information file and creates markdown and pdf versions of security assessment agreements from their inputs.

## DISCLAIMER: NO LEGAL SERVICES PROVIDED

This project cannot and does not provide legal advice. The Content is provided for general informational and educational purposes only and are not a substitute for legal advice. The information available in this repository are made in good faith, without verifying its accuracy, utility or legal validity, and should not be relied upon as the sole basis for making decisions. The authors are not a law firm, they do not engage in the practice of law, and do not act as your lawyer or provide legal advice or representation.

You are responsible for making independent determinations about the information you receive from this project, and reliance on any such information provided is solely at your own risk and does not ensure a successful legal outcome. We do not provide any kind of legal advice, explanation, opinion or recommendation to you about: (1) your possible legal rights, remedies or defenses; (2) your options, selection of forms or strategies; or (3) the legal accuracy, sufficiency or completeness of any information or answers you provide. Your use of the content in this repository does not create or establish any attorney-client relationship. Any information you submit to us or the repository is not protected by attorney-client privilege.

The law changes over time and can vary from jurisdiction to jurisdiction, and courts can give varying interpretations depending upon the situation to which the law is applied. No warranty, representation, or guarantee is being made that any legal information provided via this project is accurate, complete, exhaustive, reliable, current, appropriate, useful or fit for a particular service. Accordingly, before taking any actions based upon such information, we encourage you to confer with appropriate legal counsel or other professionals, as you deem necessary. UNDER NO CIRCUMSTANCE SHALL WE HAVE ANY LIABILITY TO YOU FOR ANY RELIANCE ON INFORMATION, DOCUMENTS OR FORMS CONTAINED ON OR OBTAINED THROUGH THIS PROJECT. SUCH RELIANCE SHALL BE SOLELY AT YOUR OWN RISK.

Installation
------------

Clone the repository
```
git clone https://github.com/seamustuohy/safetag_agreement_generator.git
```

Install python3 and pip
```
sudo apt install python3 python3-pip pandoc texlive-latex-recommended texlive-fonts-recommended
```

Install Jinja2
```
sudo -H pip3 install Jinja2
```


Assessment Agreement Templates
------------------------------

Plain Language Summary Templates and Explicit Rights and Responsibility Statement Templates.

SAFETAG Assessors operate in legal jurisdictions all over the world and in a variety of languages. The language used in each of these Assessment Agreement Templates will focus on clarity and conciseness instead of legalese. The size of the proposed engagement puts the creation of internationally applicable legal language out of scope. By clearly articulating the scope and intent of the each component lawyers in different regions will be able to evaluate and update the language to support their legal code.


### Plain Language Summary Templates

Concise plain language summary agreement templates for each agreement section.

-   Concise “plain language summary” agreement templates for the primary agreement decisions an assessor must make.

The templates will consist of readable, informal, and lively text that provide broad summaries of the agreements conditions. These summaries will be designed so that an recipient can easily become orientated to the agreement and understand the meaning of each section.

This language will be specific enough to allow an recipient to quickly identify sections of the agreement where they disagree or desire a greater level of specificity in the rights and responsibilities of each party.

#### Default Plain Templates

The repository comes with an example plain language template. It includes a "base" outline template `plain_base.j2` and a fine-grained template file `plain.j2` that extends this base. By editing the base template a assessor can add/remove large sections of the agreement without searching through the fine-grained template for the text they wish to remove.

```
└── templates
    ├── plain_base.j2
    └── plain.j2
```


The PDF and Markdown versions of these outputs can be found in the `outputs` directory.

```
└── outputs
    ├── plain_example.md
    └── plain_example.pdf
```

The variable files used to populate the fake data used in this template can be found in the variables directory. The fake data is not intended to be seen as guidance, or even as a 'good' example of an assessment.

```
└── variables
    └── plain_example.py
```

#### Creating Plain Templates

If you have changed a plain variable file or template you can re-compile the outputs by running the agreement maker.

```
python3 make_agreement.py
```

### Explicit Rights and Responsibility Statement Templates

Concise explicit rights and responsibility statement templates for each agreement section.

-   Explicit rights and responsibility statement templates for the primary agreement decisions an assessor must make.

Concise explicit rights and responsibility statement templates will be created for each agreement section. These will consist of readable, clearly structured text that clearly articulate the rights and responsibilities of each party.

SAFETAG agreements are -by nature- complex. They must convey the rights and responsibilities of both the assessor and the recipient. The sensitive and complex nature of a security assessment demands that an recipient understands and appreciates the gravity of what they are agreeing to.

#### Default Explicit Templates

The repository comes with an example explicit language template. It includes a "base" outline template `explicit_base.j2` and a fine-grained template file `explicit.j2` that extends this base. By editing the base template a assessor can add/remove large sections of the agreement without searching through the fine-grained template for the text they wish to remove.

```
└── templates
    ├── explicit_base.j2
    └── explicit.j2
```

The PDF and Markdown versions of these outputs can be found in the `outputs` directory.


```
└── outputs
    ├── explicit_example.md
    └── explicit_example.pdf
```

The variable files used to populate the fake data used in this template can be found in the variables directory. The fake data is not intended to be seen as guidance, or even as a 'good' example of an assessment.

```
└── variables
    └── explicit_example.py
```


#### Creating Explicit Templates

If you have changed an explicit variable file or template you can re-compile the outputs by running the agreement maker.

```
python3 make_agreement.py
```

### Meta-Data

-   Meta-data for each template that associate it to the broad assessment concepts and/or activities that rely on it.

Each of these Assessment Agreement Templates will be accompanied by meta-data that will allow future modules to automatically include or exclude specific agreement sections based upon the activities or excises that are used in an assessment.

For example; a meta-data tag for \*network-scanning\* could be assigned to exercises where the assessor is using software to scan the internal networks of an organization. The agreement language that is tagged network-scanning would include sections on data retention, emergency contacts, incident response, and liability for assessor induced system failures.

#### Where can I find the meta-data?

The structure of the meta-data to be used in SAFETAG is still in active flux. As such, it is more important to **show** the meta-data in action, than to assign a taxonomy to the text that would later have to be translated into another meta-data format. As such, the decision was made to represent the meta-data within this project as a combination of "conditional statements" found in the Jinja2 templates and user-assigned "variables" that are used to drive the document creation.

The template files use conditional statements to include (or not) different blocks of text based upon the variable file. In the following example the template looks to see if there is an expenses section in the variables file. If there is an expenses section then the markdown text within the conditional will be included. If there is not, it won't be included.

```
{% if expenses is not none %}
* expenses already incurred, including those from documented non-cancelable commitments. Assessor agrees to use the best efforts to minimize such costs and expenses.
{% endif %}
```

#### Customizing Meta-Data

Meta-Data files are contained in the `variable` directory.

```
└── variables
    ├── plain_example.py
    └── explicit_example.py
```

Each of these files is structured as a python object. Any additions to the meta-data need to be added to the `objects` dictionary. All variables that are used by the templates are found within this dictionary.

Agreement Decision Trees
------------------------

A set of decision support tools for SAFETAG agreement creation.

-   Structured data files (e.g. JSON, CSV, etc.) for an “agreement wide decision tree” and “section level decision trees” for each of its sections.

-   Source code that transforms the structured data into a visualization of the decision trees.

Agreement Decision Trees will allow assessors to more easily customize their agreements to match their assessment activities.

These decision trees will provide a SAFETAG assessor with a tree-like model of key decisions to be made based upon the structure of their assessment and relationship with the recipient. Each decision tree will, once analyzed, indicate the appropriate template language that an assessor should include in their agreement. These decision trees will reduce the complexity of the current agreement creation process and support the future modularity of SAFETAG content.

The decision trees will not provide the costs and benefits for each decision in the tree. These trade-offs differ widely based upon the context of an assessment. Just a few of the complex considerations that make this a such a complex task include an assessor’s relationship with an organization, the type of assessment being provided, and the source of funding.

#### Default Decision Trees (TODO)

#### Creating Decision Trees (TODO)


Project Structure
-----------------

```
.
├── LICENSE
├── make_agreement.py
├── outputs
│   ├── explicit_example.md
│   ├── explicit_example.pdf
│   ├── plain_example.md
│   └── plain_example.pdf
├── README.md
├── templates
│   ├── explicit_base.j2
│   ├── explicit.j2
│   ├── plain_base.j2
│   └── plain.j2
└── variables
    ├── explicit_example.py
    ├── __init__.py
    └── plain_example.py

```
