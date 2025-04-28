# Sum Calculator Module - GitHub & Odoo.sh Deployment Instructions

## Directory Structure

First, create this directory structure for your module:

```
sum_calculator/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── sum_calculator.py
├── views/
│   └── sum_calculator_views.xml
└── security/
    └── ir.model.access.csv
```

## GitHub Setup

1. Create a new repository on GitHub

2. Clone the repository locally:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

3. Create the directory structure and add all the files

4. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Initial commit for sum calculator module"
   git push origin main
   ```

## Odoo.sh Deployment

1. Login to your odoo.sh account

2. Create a new project or use an existing one

3. Connect your GitHub repository to the odoo.sh project

4. Build your project with the branch containing your module

5. Once deployed, install the "Sum Calculator" module from the Apps menu in Odoo

## Testing in Odoo

After installation:

1. Navigate to the "Sum Calculator" menu item
2. Create a new record
3. Enter two numbers
4. Observe that the sum is automatically calculated
