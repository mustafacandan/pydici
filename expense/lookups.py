# coding:utf-8
"""
Ajax custom lookup
@author: Sébastien Renard <Sebastien.Renard@digitalfox.org>
@license: AGPL v3 or newer (http://www.gnu.org/licenses/agpl-3.0.html)
"""

from datetime import date, timedelta

from pydici.expense.models import Expense



class RecentChargeableExpenseLookup(object):
    def get_query(self, q, request):
        """ return a query set.  you also have access to request.user if needed """
        # Only return chargeable expense of last 6 months
        return Expense.objects.filter(chargeable=True, expense_date__gt=(date.today() - timedelta(30 * 6)))

    def format_result(self, expense):
        """ the search results display in the dropdown menu.  may contain html and multiple-lines. will remove any |  """
        return u"%s (%s %s)" % (expense, expense.user.first_name, expense.user.last_name)

    def format_item(self, expense):
        """ the display of a currently selected object in the area below the search box. html is OK """
        return u"%s (%s %s)" % (expense, expense.user.first_name, expense.user.last_name)

    def get_objects(self, ids):
        """ given a list of ids, return the objects ordered as you would like them on the admin page.
            this is for displaying the currently selected items (in the case of a ManyToMany field)
        """
        return Expense.objects.filter(pk__in=ids).order_by("expense_date")