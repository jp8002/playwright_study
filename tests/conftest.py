import pytest
#Configuração do contexto do playwright, permitindo que os testes sejam executados em tela cheia.
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
		**browser_context_args,
  		"viewport":{
			"width":1900,
   			"height":1050
		}
	}
    
import pytest
from playwright.sync_api import Browser, Page

@pytest.fixture
def py_page(browser: Browser, request):
    # 1. Cria o contexto com vídeo habilitado
    context = browser.new_context(
        storage_state="state.json", 
        viewport={"width": 1900, "height": 1050},
        record_video_dir=f"test-results/tests-test-suit-py-{request.node.name}/"
    )
    
    # 2. Inicia a gravação do Trace (equivalente ao --tracing on)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    page = context.new_page()
    
    yield page
    
    # 3. Pós-teste (Teardown): Salva o trace e fecha o contexto
    # Verifica se o teste falhou para decidir se tira o screenshot final
    
    page.screenshot(path=f"test-results/tests-test-suit-py-{request.node.name}/test-finished.png", full_page=True)
    
    # Salva o arquivo de trace na pasta test-results/traces/
    context.tracing.stop(path=f"test-results/tests-test-suit-py-{request.node.name}/trace.zip")
    
    context.close()
