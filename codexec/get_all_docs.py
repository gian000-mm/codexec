import frappe

frappe.whitelist(allow_guest = False)
def get_all_docs(doctype):
    return frappe.get_all(doctype, fields=["*"])

frappe.response["data"] = {
    "ecopan_customer": get_all_docs("Ecopan Customer"),
    "ecopan_ssp": get_all_docs("Ecopan SSP")
}
