from django.http import HttpResponse
from django.shortcuts import render
from .forms import SimpleForm
import ldap

attrs = ['*']


def ldapfunc(ip, port, username, password, base, filter):
    try:
        server_uri = "ldap://" + ip + ":" + port
        name = 'cn=' + username + ',' + base
        connection = ldap.initialize(server_uri)
        if username == "" or password == "":
            connection.simple_bind_s()
        else:
            connection.set_option(ldap.OPT_REFERRALS, 0)
            connection.simple_bind_s(name, password)
        results = connection.search_s(
            base,
            ldap.SCOPE_SUBTREE,
            filter,
            attrs,
        )
        result = ""
        resnm  = 0
        for res in results:
            resnm  += 1
            result += "Result[" + str(resnm) + "]\n"
            result += str(res[0])
            result += "\n"
            result += str(res[1]).replace("b'", "'")
        connection.unbind()
        return result

    except Exception as e:
        return e


def search(request):
    if request.method == 'POST':
        form = SimpleForm(request.POST)
        result = ldapfunc(form.data['ldap_ip'], form.data['ldap_port'], form.data['username'], form.data['password'], form.data['search_base'], form.data['search_filter'])

        if form.is_valid():
            return render(request, 'eldap/search.html', {'form': form, 'result': result})

    else:
        form = SimpleForm()
        result = ""

    return render(request, 'eldap/search.html', {'form': form, 'result': result})


def payloads(request):
    return render(request, 'eldap/payloads.html')