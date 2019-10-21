
Find AWS CloudFormation-stacks which are not deployed by CodePipline


## Assumptions:

+ Assuming python is installed on your system.
+ Working profiles are configured in `~/.aws/config`
+ [boto3](https://pypi.org/project/boto3/) is installed on your system.


## Installation

### For Development

```
pip install -r requirements-devel.txt
python setup.py develop
```

### From Source

```
pip install -r requirements.txt
python setup.py install
```

### From PyPi

Install `aws-check-codepipeline-deployed-stacks` on your system using:

```
pip install aws-check-codepipeline-deployed-stacks
```

## Usage

Get basic usage info: `aws-check-codepipeline-deployed-stacks --help`

### Examples

Execute on profiles which name regex-matches `private.+staging`:

`aws-check-codepipeline-deployed-stacks --filter 'private.+staging'`
