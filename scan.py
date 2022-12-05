import os
import nmap
import webbrowser

# Create the "report" folder if it does not exist
if not os.path.exists('report'):
    os.mkdir('report')

print('Choose between a single target or a list of targets:')
print('1. Single target')
print('2. List of targets')

selection = input('Enter your selection (1 or 2): ')

if selection == '1':
    host = input('Enter the host to scan: ')

    hosts = [host]
elif selection == '2':
    filename = input('Enter the name of the file containing the list of hosts: ')

    with open(filename) as f:
        hosts = f.read().splitlines()
else:

    print('Invalid selection. Please try again.')
    exit()

nm = nmap.PortScanner()

# Open an HTML file for writing
with open('report/report.html', 'w') as f:
    f.write('<html>\n')
    f.write('<head>\n')
    f.write('<link rel="stylesheet" type="text/css" href="../style.css">\n')
    f.write('<title>Nmap Scan Results</title>\n')
    f.write('</head>\n')
    f.write('<body>\n')

    for host in hosts:
        results = nm.scan(host, arguments='-sV')

        for host in results['scan']:
            f.write('<h1>Host: {}</h1>\n'.format(host))
            f.write('<table>\n')
            f.write('<tr><th>Port</th><th>State</th><th>Service</th><th>Version</th></tr>\n')

            for port in results['scan'][host]['tcp']:
                state = results['scan'][host]['tcp'][port]['state']
                service = results['scan'][host]['tcp'][port]['name']
                version = results['scan'][host]['tcp'][port]['product']

                f.write('<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>\n'.format(port, state, service, version))

            f.write('</table>\n')

    f.write('</body>\n')
    f.write('</html>\n')

# Open the HTML file in the default web browser
webbrowser.open('report/report.html')
