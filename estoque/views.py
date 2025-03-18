from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm

def lista_produtos(request):
    query = request.GET.get('q')  
    min_qtd = request.GET.get('min_qtd')  
    max_qtd = request.GET.get('max_qtd')  
    min_preco = request.GET.get('min_preco')  
    max_preco = request.GET.get('max_preco')  

    produtos = Produto.objects.all()
    LIMITE_ESTOQUE_BAIXO = 5  # Definição do limite

    if query:
        produtos = produtos.filter(nome__icontains=query)
    if min_qtd:
        produtos = produtos.filter(quantidade__gte=min_qtd)
    if max_qtd:
        produtos = produtos.filter(quantidade__lte=max_qtd)
    if min_preco:
        produtos = produtos.filter(preco__gte=min_preco)
    if max_preco:
        produtos = produtos.filter(preco__lte=max_preco)

    return render(request, 'estoque/lista_produtos.html', {
        'produtos': produtos,
        'query': query,
        'min_qtd': min_qtd,
        'max_qtd': max_qtd,
        'min_preco': min_preco,
        'max_preco': max_preco,
        'limite_estoque_baixo': LIMITE_ESTOQUE_BAIXO,  # Passando para o template
    })

def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'estoque/adicionar_produto.html', {'form': form})

def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'estoque/editar_produto.html', {'form': form, 'produto': produto})

def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'estoque/excluir_produto.html', {'produto': produto})
