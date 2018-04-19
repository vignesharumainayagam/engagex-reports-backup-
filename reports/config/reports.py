from frappe import _

def get_data():
	return [
		{
			"label": _("Accounts"),
			"icon": "fa fa-table",
			"items": [
				{
					"type": "report",
					"name": "Trial Balance for Party",
					"doctype": "GL Entry",
					"is_query_report": True,
				},
				{
					"type": "report",
					"name": "Profitability Analysis",
					"doctype": "GL Entry",
					"is_query_report": True,
				},
			]
		},
		{
			"label": _("CRM"),
			"icon": "fa fa-list",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Lead By Owner",
					"doctype": "Lead"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Lead Converted By Owner",
					"doctype": "Lead"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Leads by Course",
					"doctype": "Lead"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Leads By Status",
					"doctype": "Lead"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Lead Details",
					"doctype": "Lead"
				},
				{
					"type": "page",
					"name": "sales-funnel",
					"label": _("Sales Funnel"),
					"icon": "fa fa-bar-chart",
				},
				{
					"type": "report",
					"name": "Prospects Engaged But Not Converted",
					"doctype": "Lead",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Minutes to First Response for Opportunity",
					"doctype": "Opportunity",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Month Sales(student conversion)",
					"doctype": "Opportunity",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Sales Cycle Duration Across Staffs",
					"doctype": "Opportunity",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Sources Conversion",
					"doctype": "Opportunity",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Today's Sales(student conversion)",
					"doctype": "Opportunity",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Todays Calls Report(Branch)",
					"doctype": "Opportunity",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Todays Calls Report(Branch)",
					"doctype": "Opportunity",
					"is_query_report": True
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Weekly Sales(student conversion)",
					"doctype": "Contact"
				},
		
			]
		},
		{
			"label": _("Education"),
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Student and Guardian Contact Details",
					"doctype": "Program Enrollment"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Absent Student Report",
					"doctype": "Student Attendance"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Student Batch-Wise Attendance",
					"doctype": "Student Attendance"
				},		
				{
					"type": "report",
					"is_query_report": True,
					"name": "Student Monthly Attendance Sheet",
					"doctype": "Student Attendance"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Course wise Assessment Report",
					"doctype": "Assessment Result"
				},		
				{
					"type": "report",
					"is_query_report": True,
					"name": "Assessment Plan Status",
					"doctype": "Assessment Plan"
				},
				{
					"type": "report",
					"name": "Student Fee Collection",
					"doctype": "Fees",
					"is_query_report": True
				},
			]
		},
		{
			"label": _("HR"),
			"icon": "fa fa-list",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Employee Leave Balance",
					"doctype": "Leave Application"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Employee Birthday",
					"doctype": "Employee"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Employees working on a holiday",
					"doctype": "Employee"
				},
				{
					"type": "report",
					"name": "Employee Information",
					"doctype": "Employee"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Salary Register",
					"doctype": "Salary Slip"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Monthly Attendance Sheet",
					"doctype": "Attendance"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Vehicle Expenses",
					"doctype": "Vehicle"
				},

			]
		},

	]
