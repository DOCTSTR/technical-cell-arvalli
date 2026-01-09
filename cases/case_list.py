<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>

<h2>{{ title }}</h2>

<table border="1" cellpadding="8" cellspacing="0">
    <tr>
        <th>FIR Number</th>
        <th>Police Station</th>
        <th>Incident Date</th>
        <th>Status</th>
    </tr>

    {% for case in cases %}
    <tr>
        <td>{{ case.fir_number }}</td>
        <td>{{ case.police_station }}</td>
        <td>{{ case.incident_date }}</td>
        <td>{{ case.status|title }}</td>
    </tr>
    {% empty %}
    <tr>
        <td colspan="4">No cases found</td>
    </tr>
    {% endfor %}
</table>

<br>
<a href="/dashboard/">⬅ Back to Dashboard</a>

</body>
</html>
