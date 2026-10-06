from rich.console import Console
from rich.panel import Panel
from rich.align import Align
import requests
import time
import os
import json
import uuid

console = Console()


def header():
    os.system("cls" if os.name == "nt" else "clear")
    console.print()
    
    banner = """[bold red]
  ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
  ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
  ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║
  ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║
  ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝
  ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
[/bold red]"""
    
    console.print(banner)
    console.print(Align.center("[bold white on red]  Discord Reporter v1  [/bold white on red]"))
    console.print()
    console.print(Align.center("[bold cyan]https://github.com/xhamzawi[/bold cyan]"))
    console.print()
    console.print("[bold red]═══════════════════════════════════════════════════[/bold red]")
    console.print()


def generate_installation_id():
    """Generate a Discord-like installation ID"""
    snowflake = str(int(time.time() * 1000))
    token = uuid.uuid4().hex[:22]
    return f"{snowflake}.{token}"


def send_report(token, user_id, installation_id=None):
    """Send a single report using the correct endpoint /api/v9/reporting/user"""
    if installation_id is None:
        installation_id = generate_installation_id()

    url = "https://discord.com/api/v9/reporting/user"

    headers = {
        "Host": "discord.com",
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Origin": "https://discord.com",
        "Referer": "https://discord.com/channels/@me",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "X-Discord-Locale": "en-US",
        "X-Discord-Timezone": "Asia/Baghdad",   # change if needed
        "X-Debug-Options": "bugReporterEnabled",
        "X-Installation-Id": installation_id,
        "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiaGFzX2NsaWVudF9tb2RzIjpmYWxzZSwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzE1MS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTUxLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL2Rpc2NvcmQuY29tLz9kaXNjb3JkdG9rZW49TVRVek9EZ3pOVEUxTmpFeU5UYzBPVEk0T0EuR1BDVFdoLjNTa19rRUFzcm94b052SmEwSUhtNk9RaG50SFMxX3JHaEVlUkhZIiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vZGlzY29yZC5jb20vIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiZGlzY29yZC5jb20iLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo2Mjk3NzksImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGwsImNsaWVudF9sYXVuY2hfaWQiOiIyOWVhNzYxMy0yODhlLTQ2MmQtOTQ2MC01ODM5MzU1Njc0ZTIiLCJsYXVuY2hfc2lnbmF0dXJlIjoiZGY0N2ViYzktNjM2My00NTg5LThjNTYtMDkxNzA4NGVlMDg2IiwiY2xpZW50X2FwcF9zdGF0ZSI6ImZvY3VzZWQiLCJjbGllbnRfaGVhcnRiZWF0X3Nlc3Npb25faWQiOiJkODFlNThjYi0xMzVmLTQ1YjctOTk2Ny1mNTVlMDMzYjIwMmQifQ==",
    }

    payload = {
        "version": "1.0",
        "variant": "4",
        "language": "en",
        "breadcrumbs": [63, 22, 19, 25],
        "elements": {
            "user_profile_select": ["photos", "name", "descriptors", "server_tag"]
        },
        "user_id": str(user_id),
        "name": "user"
    }

    try:
        r = requests.post(url, headers=headers, json=payload, timeout=15)
        return r.status_code, r.text
    except requests.exceptions.Timeout:
        return None, "Request timeout"
    except requests.exceptions.ConnectionError:
        return None, "Connection error"
    except Exception as e:
        return None, str(e)


def format_seconds(seconds):
    seconds = int(seconds)
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    if h > 0:
        return f"{h}h {m}m {s}s"
    elif m > 0:
        return f"{m}m {s}s"
    else:
        return f"{s}s"


def countdown(seconds, label="Rate limited"):
    total = int(seconds)
    for remaining in range(total, 0, -1):
        console.print(
            f"\r  [bold yellow]⏳ {label}[/bold yellow] "
            f"[white]— retry in[/white] "
            f"[bold cyan]{format_seconds(remaining)}[/bold cyan]   ",
            end=""
        )
        time.sleep(1)
    console.print("\r" + " " * 60 + "\r", end="")


def show_error(title, body):
    console.print()
    console.print(
        Panel(
            body,
            title=f"[bold red]✗ {title}[/bold red]",
            border_style="red",
            padding=(0, 2),
        )
    )
    console.print()


def main():
    header()


    token = console.input("  [bold green]Discord token  :[/bold green] ").strip()
    if not token:
        console.print("\n  [bold red]✗ Token is required![/bold red]\n")
        return

    user_id = console.input("  [bold green]Target Userid  :[/bold green] ").strip()
    if not user_id:
        console.print("\n  [bold red]✗ Target Userid is required![/bold red]\n")
        return

    delay_input = console.input("  [bold green]Sleep (delay)  :[/bold green] ").strip()
    try:
        delay = float(delay_input) if delay_input else 2.0
        if delay < 0:
            delay = 2.0
    except ValueError:
        delay = 2.0

    installation_id = generate_installation_id()

    console.print()
    console.print("  [bold red]═══════════════════════════════════════════════════[/bold red]")
    console.print("  [bold yellow]Starting reporter...[/bold yellow]")
    console.print()

    count = 0
    rate_limit_count = 0

    while True:
        try:
            status, text = send_report(token, user_id, installation_id)

            if status is None:
                show_error("CONNECTION ERROR", f"[bold white]{text}[/bold white]")
                break

            try:
                data = json.loads(text)
            except Exception:
                data = {}

            # ── Rate Limit (429) ──
            if status == 429 or (
                isinstance(data, dict) and "rate limited" in str(data.get("message", "")).lower()
            ):
                rate_limit_count += 1
                retry_after = data.get("retry_after", 60) if isinstance(data, dict) else 60
                is_global = data.get("global", False) if isinstance(data, dict) else False

                console.print()
                console.print(
                    Panel(
                        f"[bold white]The resource is being rate limited.[/bold white]\n"
                        f"[dim]Type    :[/dim] [bold yellow]{'Global' if is_global else 'User'}[/bold yellow]\n"
                        f"[dim]Retry in:[/dim] [bold cyan]{format_seconds(retry_after)}[/bold cyan]\n"
                        f"[dim]Occurred:[/dim] [bold magenta]{rate_limit_count}[/bold magenta] time(s)",
                        title="[bold yellow]⚠ RATE LIMITED[/bold yellow]",
                        border_style="yellow",
                        padding=(0, 2),
                    )
                )
                console.print()

                countdown(retry_after, label="Rate limited")
                console.print("  [bold green]✓ Resuming reports...[/bold green]")
                console.print()
                continue

            # ── Invalid Token (401) ──
            if status == 401 or "401: Unauthorized" in text:
                show_error(
                    "ERROR",
                    "[bold white]401: Unauthorized[/bold white]\n"
                    "[dim]Your Discord token is invalid or expired.[/dim]"
                )
                break

            # ── User not found ──
            if "Could not find user" in text or (
                isinstance(data, dict) and "Could not find user" in str(data.get("message", ""))
            ):
                show_error(
                    "ERROR",
                    f"[bold white]Could not find user:[/bold white] [bold yellow]{user_id}[/bold yellow]\n"
                    f"[dim]Make sure the user ID is correct.[/dim]"
                )
                break

            # ── Successful report ──
            if isinstance(data, dict) and "report_id" in data:
                count += 1
                report_id = data["report_id"]
                console.print(
                    f"  [bold green]✓[/bold green] [bold white]Report Done[/bold white] "
                    f"[bold yellow]#{count}[/bold yellow] : [bold cyan]{report_id}[/bold cyan]"
                )

            # ── Empty 200 / 204 success ──
            elif status in (200, 201, 204) and not text.strip():
                count += 1
                console.print(
                    f"  [bold green]✓[/bold green] [bold white]Report Done[/bold white] "
                    f"[bold yellow]#{count}[/bold yellow] : [dim]No ID returned[/dim]"
                )

            elif isinstance(data, dict) and "message" in data and "code" in data:
                show_error("ERROR", f"[bold white]{data['message']}[/bold white]")
                break

            else:
                console.print(f"  [bold yellow]⚠ Unknown response:[/bold yellow] [dim]{text[:200]}[/dim]")

            time.sleep(delay)

        except KeyboardInterrupt:
            console.print()
            console.print(
                f"  [bold cyan]■ Stopped — "
                f"Total reports sent: [bold yellow]{count}[/bold yellow][/bold cyan]"
            )
            console.print()
            break
        except Exception as e:
            console.print(f"  [bold red]✗ Unexpected error: {e}[/bold red]")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n  [bold red]Bot stopped.[/bold red]\n")
