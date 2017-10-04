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
sudo apt install python3 python3-pip pandoc texlive-latex-recommended texlive-fonts-recommended python3-tk graphviz
```

Install Jinja2
```
sudo -H pip3 install Jinja2
```

Install graph creation libraries
```
sudo -H pip3 install pygraphviz networkx
```


Install DataPackage (1.0)
This was written right before the 1.0 breaking release of datapackage. If your version of pip has the 1.0+ version of data package in it you can install it using pip. ```sudo -H pip3 install datapackage``` If it does not, then you will have to follow the below instructions.
```
cd /tmp
git clone https://github.com/frictionlessdata/datapackage-py.git
cd datapackage-py
sudo -H python3 setup.py install
```


Agreement Decision QuickStart: Interactive Graphical User Interface (GUI)
-------------------------------------------------------------------

The SAFETAG agreement generator includes an interactive agreement decision making tool that allows assessors to more easily customize their agreements to match their recipient, context, activities, fees, and a variety of other factors. This GUI can be started by running the following command.

```
python3 make_agreement.py
```

![screenshot of interface](https://github.com/seamustuohy/safetag_agreement_generator/blob/decision_tree/images/screenshot.png?raw=true)

Once the Assessor has finished entering data in the GUI a new "custom variable" file will be create in the "variables" folder. It will be named `custom_[DATE]_[TIME].json` (for example: `custom_2017_Sep_10_13_17.json`.) You can learn more about the structure of this variable file in the **Variable Files** section below.


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
├── outputs
│   ├── plain_custom.md
│   └── plain_custom.pdf

```

#### Creating Plain Agreements

If you have used the GUI to create a new decisions file or you have customized the template you can re-compile the outputs by running the agreement maker.

```
python3 make_agreement.py -p variables/my_custom_agreement_decisions.json -a plain
```

make_agreement.py has the following optional arguments:

```
  -h, --help            show this help message and exit
  --verbose, -v         Turn verbosity on
  --debug, -d           Turn debugging on
  --parse PARSE, -p PARSE
                        Path to an existing custom agreement document to parse
                        into an agreement. This will re-read the custom
                        agreement values from this file as well as from the
                        entity files. As such, this will execute the template
                        without the decision tree questions. This enables you
                        to tweak your agreement json file and/or your entity
                        csv files to re-generate your agreements quickly.
  --agreement_type AGREEMENT_TYPE, -a AGREEMENT_TYPE
                        The type of agreement template to use. (plain,
                        explicit, or both) The default is both.
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
├── outputs
│   ├── explicit_custom.md
│   └── explicit_custom.pdf

```

#### Creating Explicit Agreements

If you have used the GUI to create a new decisions file or you have customized the template you can re-compile the outputs by running the agreement maker.

```
python3 make_agreement.py -p variables/my_custom_agreement_decisions.json -a explicit
```

*If you don't use the -a flag it will produce both the explicit and plain custom agreements.*



### Variable Files: Agreement Entities & Custom Meta-Data

The templates use "variable" files to include or exclude specific agreement sections and populate the contents of an agreement. These variable files come in two forms "Entities" and "Custom Meta-Data". The "Custom Meta-Data" file is what is populated by the SAFETAG agreement generator. The "Entities" are CSV (Comma Separated Value) files that you fill with structured data about different aspects of your agreement.

#### The Example Variable Files

The variable files used to populate the fake data used in the example outputs can be found in the variables directory. **The fake data is not intended to be seen as guidance or even as examples of 'appropriate practice'.** These variable files can be used to see exactly how the templates were filled in.


```
└── variables
    ├── entities
    │   ├── activities.csv
    │   ├── data_handling.csv
    │   ├── deliverables.csv
    │   ├── milestones.csv
    │   ├── rates.csv
    │   ├── representations_and_warranties.csv
    │   └── representatives.csv
    └── custom_example.json

```


#### Entity Variable Files

The Entity variable files are used by an auditor to

These variable files are accompanied by a [Data Package](http://frictionlessdata.io/data-packages/) `variables/datapackage.json` that describes each of their formats and provides guidance on what each field within them should contain. When the agreement is being created this data-package is also used to validate that these Entity files are properly formatted. ([It follows the Tabular Data Package structure.](http://frictionlessdata.io/guides/tabular-data-package/))

```
└── variables
    ├── entities
    │   ├── activities.csv
    │   ├── data_handling.csv
    │   ├── deliverables.csv
    │   ├── milestones.csv
    │   ├── rates.csv
    │   ├── representations_and_warranties.csv
    │   └── representatives.csv
    └── datapackage.json

```

#### Customizing Meta-Data

Meta-Data files are contained in the `variable` directory.

```
└── variables
    ├── plain_example.py
    └── explicit_example.py
```

Each of these files is structured as a python object. Any additions to the meta-data need to be added to the `objects` dictionary. All variables that are used by the templates are found within this dictionary.



#### Agreement Decision Trees

A visualization of the SAFETAG agreement decision tree. This includes transforming a structured decision data file (see: Agreement Decision GUI) into an agreement wide decision tree that shows how decision build upon each other.

This agreement decision tree, when looked at in relation to the agreement templates, will allow assessors to more explore how they can customize their agreements to match their assessment activities.

A pre-built decision tree can be found in the outputs directory.

```
└── outputs
    └── decision_tree.svg
```


This tree, when opened in a users browser, shows
* Each individual question that a user will have to answer;
* How the answer to these questions open up further questions; and
* The help text for those questions (if the user hovers over a question with their mouse.)

If the user decides to their own decisions to the core decision data file and templates this tree, like the GUI, is able to be easily updated to use the new decisions. The following command re-compiles the decision tree SVG when run.

```python
python3 make_agreement.py --graph
```

The decision trees will not provide the costs and benefits for each decision in the tree. These trade-offs differ widely based upon the context of an assessment. Just a few of the complex considerations that make this a such a complex task include an assessor’s relationship with an organization, the type of assessment being provided, and the source of funding.


#### Agreement Decision GUI

The SAFETAG agreement generator includes an interactive agreement decision making tool that allows assessors to more easily customize their agreements to match their assessment activities.

The GUI transforms a structured decision tree file `variables/decision.json` into an interactive decision support tool where an Assessors decisions determine the agreement that will be created and the information they have to provide.

```
└── variables
    └── decisions.json

```


* question: The question to as the user.
* help: Help text to show the user when answering this question.
* sets: The variable name to assign this decision to.

```json
  "term_of_contract": [
    {
      "question": "What is the start date of the Agreement?",
      "help": "The start date of the Agreement is not necessarily the start date of the Assessment.",
      "sets": "agreement_start_date"
    },
```

* answers: Multiple choice answers to choose from. (dict)
  * {"user facing description":"value to set variable to when chosen"}

```json
    {
      "question": "What event(s) will signal that the agreement is completed?",
      "sets": "event_that_completes_agreement",
      "answers": {
        "A certain date": "date",
        "The scope of work and deliverables are complete": "sow",
        "Both the date and the completion of deliverables and scope of work": "both"
      }
    }
```

* depends: Answer/Value pairs from this section that determine if a question is asked (dict)
  * {"previous question `sets` variable name", "value it must be set to to show this question"}
  * Special Option: "type"
    * The "type" option allows you to determine if multiple variables in the depends section are evaluated using an "and" operation "depends on X and Y" or a "or" operation "depends on X or Y".
    * {"type": "or"}

```json
    {
      "question": "What is the end date of the Agreement",
      "sets": "agreement_end_date",
      "depends": {
        "type": "or",
        "event_that_completes_agreement": "both"
      }
    }
```


* from_package: The datapackage that this question represents.
  * {"name": "the datapackages name according to the datapackage.json file"}
  * Special Option: "conditions"
    * The "conditions" option defines a subset of values from a datapackage that should be used (uses an "and" operation.)
    * "conditions" { "work_type": "deliverable_revision" }
    * *NOTE: This does nothing in the current GUI based implementation. The text user interface (TUI) has code that would parse these operations and set them to the from_package variables. But, this logic currently resides in the Jinja template files.*
* take_input: Should this decision show up in the user interface? Set to false if the decision is a datapackage. (bool)


```json
    {
      "question": "What guidelines will be followed for securing devices used during the assessment?",
      "help": "You need to set these in the data_handling.csv file using \"devices\" in the \"security focus\" column and \"service_provider\", \"recipiant\", or \"both\" in the \"responsible_parties\" column depending upon the responsible party",
      "from_package": {
        "name": "data_handling",
        "conditions": {
          "security_focus": "devices"
        }
      },
      "sets": "device_security_guidelines",
      "take_input": false
    },
```

#### Putting Meta-Data Files to work with Templates

The Meta-Data created by the Agreement GUI is put to work as a combination of "conditional statements" found in the Jinja2 templates. The template files use conditional statements to include (or not) different blocks of text based upon the variable file. In the following example the template looks to see if there is an expenses section in the variables file. If there is an expenses section then the markdown text within the conditional will be included. If there is not, it won't be included.

```
{% if expenses is not none %}
* expenses already incurred, including those from documented non-cancelable commitments. Assessor agrees to use the best efforts to minimize such costs and expenses.
{% endif %}
```
