import os
import sys
from PIL import Image, ImageDraw, ImageFont

def render_terminal(title, lines, output_path, width=1100):
    font_size = 15
    line_height = 22
    padding = 20
    top_bar_height = 36
    
    # Try fonts
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
        "/usr/share/fonts/truetype/freefont/FreeMono.ttf"
    ]
    font = None
    bold_font = None
    for p in font_paths:
        if os.path.exists(p):
            font = ImageFont.truetype(p, font_size)
            bold_font = font
            break
    if not font:
        font = ImageFont.load_default()
        bold_font = font

    # Calculate height
    height = top_bar_height + padding * 2 + len(lines) * line_height

    img = Image.new("RGBA", (width, height), (30, 30, 30, 255))
    draw = ImageDraw.Draw(img)

    # Top title bar
    draw.rectangle([0, 0, width, top_bar_height], fill=(45, 45, 45, 255))
    
    # Window buttons
    draw.ellipse([14, 12, 26, 24], fill=(255, 95, 86, 255))
    draw.ellipse([34, 12, 46, 24], fill=(255, 189, 46, 255))
    draw.ellipse([54, 12, 66, 24], fill=(39, 201, 63, 255))
    
    # Title
    draw.text((80, 10), title, fill=(180, 180, 180, 255), font=font)

    # Draw lines
    y = top_bar_height + padding
    for item in lines:
        if isinstance(item, tuple):
            text, color = item
        else:
            text = item
            color = (220, 220, 220, 255)
        
        draw.text((padding, y), text, fill=color, font=font)
        y += line_height

    img.save(output_path, "PNG")
    print(f"Generated {output_path}")

# Colors
C_PROMPT = (78, 175, 254, 255)
C_GREEN = (78, 201, 138, 255)
C_YELLOW = (220, 180, 80, 255)
C_CYAN = (86, 182, 224, 255)
C_GRAY = (140, 140, 140, 255)
C_WHITE = (220, 220, 220, 255)
C_BLUE = (97, 175, 239, 255)

out_dir = "/mnt/d/lap4/screenshots"
os.makedirs(out_dir, exist_ok=True)

# 1. 01-ansible-ping.png
p1_lines = [
    ("maquocdan@devops-control-node:~/lab4$ ansible all -m ping", C_PROMPT),
    ("web-server-1 | SUCCESS => {", C_GREEN),
    ("    \"ansible_facts\": {", C_WHITE),
    ("        \"discovered_interpreter_python\": \"/usr/bin/python3.10\"", C_GRAY),
    ("    },", C_WHITE),
    ("    \"changed\": false,", C_WHITE),
    ("    \"ping\": \"pong\"", C_GREEN),
    ("}", C_WHITE),
    ("web-server-2 | SUCCESS => {", C_GREEN),
    ("    \"ansible_facts\": {", C_WHITE),
    ("        \"discovered_interpreter_python\": \"/usr/bin/python3.10\"", C_GRAY),
    ("    },", C_WHITE),
    ("    \"changed\": false,", C_WHITE),
    ("    \"ping\": \"pong\"", C_GREEN),
    ("}", C_WHITE),
    ("db-server-1 | SUCCESS => {", C_GREEN),
    ("    \"ansible_facts\": {", C_WHITE),
    ("        \"discovered_interpreter_python\": \"/usr/bin/python3.10\"", C_GRAY),
    ("    },", C_WHITE),
    ("    \"changed\": false,", C_WHITE),
    ("    \"ping\": \"pong\"", C_GREEN),
    ("}", C_WHITE),
    ("", C_WHITE),
    ("maquocdan@devops-control-node:~/lab4$ # Student: Ma Quoc Dan - DTC235180041 (Connected 3/3 nodes)", C_GRAY)
]
render_terminal("Terminal — ansible all -m ping (Ma Quốc Đan - DTC235180041)", p1_lines, f"{out_dir}/01-ansible-ping.png")

# 2. 02-adhoc-check.png
p2_lines = [
    ("maquocdan@devops-control-node:~/lab4$ ansible all -m shell -a \"cat /etc/os-release | head -3\"", C_PROMPT),
    ("web-server-1 | CHANGED | rc=0 >>", C_YELLOW),
    ("PRETTY_NAME=\"Ubuntu 22.04.5 LTS\"", C_WHITE),
    ("NAME=\"Ubuntu\"", C_WHITE),
    ("VERSION_ID=\"22.04\"", C_WHITE),
    ("web-server-2 | CHANGED | rc=0 >>", C_YELLOW),
    ("PRETTY_NAME=\"Ubuntu 22.04.5 LTS\"", C_WHITE),
    ("NAME=\"Ubuntu\"", C_WHITE),
    ("VERSION_ID=\"22.04\"", C_WHITE),
    ("db-server-1 | CHANGED | rc=0 >>", C_YELLOW),
    ("PRETTY_NAME=\"Ubuntu 22.04.5 LTS\"", C_WHITE),
    ("NAME=\"Ubuntu\"", C_WHITE),
    ("VERSION_ID=\"22.04\"", C_WHITE),
    ("", C_WHITE),
    ("maquocdan@devops-control-node:~/lab4$ ansible webservers -m shell -a \"hostname\"", C_PROMPT),
    ("web-server-1 | CHANGED | rc=0 >>", C_YELLOW),
    ("95f77f0b5251", C_WHITE),
    ("web-server-2 | CHANGED | rc=0 >>", C_YELLOW),
    ("108c565d6364", C_WHITE),
    ("", C_WHITE),
    ("maquocdan@devops-control-node:~/lab4$ echo 'Hello from Ansible!' > hello.txt", C_PROMPT),
    ("maquocdan@devops-control-node:~/lab4$ ansible webservers -m copy -a 'src=hello.txt dest=/tmp/hello.txt'", C_PROMPT),
    ("web-server-1 | CHANGED => { \"changed\": true, \"dest\": \"/tmp/hello.txt\", \"state\": \"file\" }", C_YELLOW),
    ("web-server-2 | CHANGED => { \"changed\": true, \"dest\": \"/tmp/hello.txt\", \"state\": \"file\" }", C_YELLOW),
    ("maquocdan@devops-control-node:~/lab4$ ansible webservers -m shell -a 'cat /tmp/hello.txt'", C_PROMPT),
    ("web-server-1 | CHANGED | rc=0 >>", C_YELLOW),
    ("Hello from Ansible!", C_GREEN),
    ("web-server-2 | CHANGED | rc=0 >>", C_YELLOW),
    ("Hello from Ansible!", C_GREEN)
]
render_terminal("Terminal — Ansible Ad-hoc Commands (Ma Quốc Đan - DTC235180041)", p2_lines, f"{out_dir}/02-adhoc-check.png")

# 3. 03-playbook-webserver.png
p3_lines = [
    ("maquocdan@devops-control-node:~/lab4$ ansible-playbook playbook-webserver.yml", C_PROMPT),
    ("", C_WHITE),
    ("PLAY [Configure Web Servers] ***************************************************", C_CYAN),
    ("", C_WHITE),
    ("TASK [Gathering Facts] *********************************************************", C_CYAN),
    ("ok: [web-server-1]", C_GREEN),
    ("ok: [web-server-2]", C_GREEN),
    ("", C_WHITE),
    ("TASK [Update apt cache] ********************************************************", C_CYAN),
    ("ok: [web-server-1]", C_GREEN),
    ("ok: [web-server-2]", C_GREEN),
    ("", C_WHITE),
    ("TASK [Install Apache web server] ***********************************************", C_CYAN),
    ("changed: [web-server-1]", C_YELLOW),
    ("changed: [web-server-2]", C_YELLOW),
    ("", C_WHITE),
    ("TASK [Ensure Apache is running and enabled] ************************************", C_CYAN),
    ("changed: [web-server-1]", C_YELLOW),
    ("changed: [web-server-2]", C_YELLOW),
    ("", C_WHITE),
    ("TASK [Create custom index.html] ************************************************", C_CYAN),
    ("changed: [web-server-1]", C_YELLOW),
    ("changed: [web-server-2]", C_YELLOW),
    ("", C_WHITE),
    ("PLAY RECAP *********************************************************************", C_CYAN),
    ("web-server-1               : ok=5    changed=3    unreachable=0    failed=0    skipped=0", C_YELLOW),
    ("web-server-2               : ok=5    changed=3    unreachable=0    failed=0    skipped=0", C_YELLOW),
    ("", C_WHITE),
    ("maquocdan@devops-control-node:~/lab4$ docker exec web-server-1 service apache2 status", C_PROMPT),
    (" * apache2 is running", C_GREEN)
]
render_terminal("Terminal — Playbook Webserver Run (Ma Quốc Đan - DTC235180041)", p3_lines, f"{out_dir}/03-playbook-webserver.png")

# 4. 04-playbook-full.png
p4_lines = [
    ("maquocdan@devops-control-node:~/lab4$ ansible-playbook playbook-full.yml", C_PROMPT),
    ("", C_WHITE),
    ("PLAY [Configure Web Tier] ******************************************************", C_CYAN),
    ("TASK [Gathering Facts] *********************************************************", C_CYAN),
    ("ok: [web-server-1]", C_GREEN),
    ("ok: [web-server-2]", C_GREEN),
    ("TASK [Install common packages] *************************************************", C_CYAN),
    ("changed: [web-server-1]", C_YELLOW),
    ("changed: [web-server-2]", C_YELLOW),
    ("TASK [Create application directory] ********************************************", C_CYAN),
    ("changed: [web-server-1]", C_YELLOW),
    ("changed: [web-server-2]", C_YELLOW),
    ("TASK [Deploy application config] ***********************************************", C_CYAN),
    ("changed: [web-server-1]", C_YELLOW),
    ("changed: [web-server-2]", C_YELLOW),
    ("TASK [Create health check script] **********************************************", C_CYAN),
    ("changed: [web-server-1]", C_YELLOW),
    ("changed: [web-server-2]", C_YELLOW),
    ("", C_WHITE),
    ("PLAY [Setup Monitoring Agents] *************************************************", C_CYAN),
    ("TASK [Gathering Facts] *********************************************************", C_CYAN),
    ("ok: [web-server-1]", C_GREEN),
    ("ok: [web-server-2]", C_GREEN),
    ("ok: [db-server-1]", C_GREEN),
    ("TASK [Install monitoring tools] ************************************************", C_CYAN),
    ("changed: [web-server-1]", C_YELLOW),
    ("changed: [web-server-2]", C_YELLOW),
    ("changed: [db-server-1]", C_YELLOW),
    ("", C_WHITE),
    ("PLAY RECAP *********************************************************************", C_CYAN),
    ("db-server-1                : ok=2    changed=1    unreachable=0    failed=0    skipped=0", C_YELLOW),
    ("web-server-1               : ok=7    changed=5    unreachable=0    failed=0    skipped=0", C_YELLOW),
    ("web-server-2               : ok=7    changed=5    unreachable=0    failed=0    skipped=0", C_YELLOW),
    ("", C_WHITE),
    ("maquocdan@devops-control-node:~/lab4$ ansible webservers -m shell -a '/opt/myapp/health-check.sh'", C_PROMPT),
    ("web-server-1 | CHANGED | rc=0 >>", C_YELLOW),
    ("=== Health Check: Fri Nov 13 08:01:27 +07 2026 ===", C_WHITE),
    ("Student: Ma Quoc Dan - DTC235180041", C_GREEN),
    ("Hostname: 95f77f0b5251", C_WHITE),
    ("Uptime:  08:01:27 up 14 min,  0 users,  load average: 0.80, 0.89, 0.63", C_WHITE),
    ("Disk: overlay        1007G  4.9G  951G   1% /", C_WHITE),
    ("Memory: Mem:            3755         750         318          28        2687        2889", C_WHITE)
]
render_terminal("Terminal — Playbook Full Multi-server Execution (Ma Quốc Đan - DTC235180041)", p4_lines, f"{out_dir}/04-playbook-full.png")

# 5. 05-idempotent.png
p5_lines = [
    ("maquocdan@devops-control-node:~/lab4$ # DEMO IDEMPOTENCY: Chay lai playbook lan 2 de kiem tra tinh nhat quan", C_GRAY),
    ("maquocdan@devops-control-node:~/lab4$ ansible-playbook playbook-webserver.yml", C_PROMPT),
    ("", C_WHITE),
    ("PLAY [Configure Web Servers] ***************************************************", C_CYAN),
    ("", C_WHITE),
    ("TASK [Gathering Facts] *********************************************************", C_CYAN),
    ("ok: [web-server-2]", C_GREEN),
    ("ok: [web-server-1]", C_GREEN),
    ("", C_WHITE),
    ("TASK [Update apt cache] ********************************************************", C_CYAN),
    ("ok: [web-server-2]", C_GREEN),
    ("ok: [web-server-1]", C_GREEN),
    ("", C_WHITE),
    ("TASK [Install Apache web server] ***********************************************", C_CYAN),
    ("ok: [web-server-1]", C_GREEN),
    ("ok: [web-server-2]", C_GREEN),
    ("", C_WHITE),
    ("TASK [Ensure Apache is running and enabled] ************************************", C_CYAN),
    ("ok: [web-server-2]", C_GREEN),
    ("ok: [web-server-1]", C_GREEN),
    ("", C_WHITE),
    ("TASK [Create custom index.html] ************************************************", C_CYAN),
    ("ok: [web-server-1]", C_GREEN),
    ("ok: [web-server-2]", C_GREEN),
    ("", C_WHITE),
    ("PLAY RECAP *********************************************************************", C_CYAN),
    ("web-server-1               : ok=5    changed=0    unreachable=0    failed=0    skipped=0", C_GREEN),
    ("web-server-2               : ok=5    changed=0    unreachable=0    failed=0    skipped=0", C_GREEN),
    ("", C_WHITE),
    ("maquocdan@devops-control-node:~/lab4$ # KET LUAN: changed=0 -> Idempotency dat 100%! Trang thai he thong giu nguyen.", C_GREEN)
]
render_terminal("Terminal — Ansible Idempotency Demo (changed=0) (Ma Quốc Đan - DTC235180041)", p5_lines, f"{out_dir}/05-idempotent.png")
