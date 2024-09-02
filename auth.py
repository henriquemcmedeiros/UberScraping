from playwright.sync_api import sync_playwright

def get_csrf_token():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, proxy={"server": "http://localhost:8080"})
        context = browser.new_context()
        
        page = context.new_page()
        page.goto('https://auth.uber.com/login/')
        
        # Preencher o campo de email/telefone usando o id
        page.fill('input[name="email"]', 'piwebscrapping@gmail.com')

        # Clicar no botão "Next" (ou "Submit")
        page.click('button[type="submit"]')

        # Esperar o campo de senha aparecer e preenchê-lo
        page.wait_for_selector('input[type="password"]')
        page.fill('input[type="password"]', 'piteste01')

        # Clicar no botão "Submit" após preencher a senha
        page.click('button[type="submit"]')

        # Esperar a página carregar completamente
        page.wait_for_navigation()

        # Esperar a página carregar e o token estar disponível
        try:
            page.wait_for_selector('meta[name="csrf-token"]', state='visible', timeout=10000)
            csrf_token = page.get_attribute('meta[name="csrf-token"]', 'content')
            print('CSRF Token:', csrf_token)
        except Exception as e:
            print(f"Erro: {e}")
        
        # Fechar o navegador
        browser.close()

if __name__ == "__main__":
    get_csrf_token()