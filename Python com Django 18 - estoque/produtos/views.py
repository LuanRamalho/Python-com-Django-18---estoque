from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm
from django.db.models import Q
from .models import Nota
from .forms import NotaForm


def lista_produtos(request, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)
    
    # Pega o parâmetro 'q' da barra de busca (se houver)
    busca = request.GET.get('q', '')
    
    if busca:
        # Filtra produtos com base na busca (nome ou preço)
        produtos = Produto.objects.filter(
            Q(nome__icontains=busca) | Q(preco__icontains=busca), nota=nota
        )
    else:
        # Caso não haja busca, retorna todos os produtos
        produtos = Produto.objects.filter(nota=nota)
    
    return render(request, 'produtos/lista.html', {'nota': nota, 'produtos': produtos, 'busca': busca})


def adicionar_produto(request, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)  # Obtém a nota associada
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.nota = nota  # Relaciona o produto à nota
            produto.save()
            return redirect('lista_produtos', nota_id=nota.id)  # Redireciona corretamente
    else:
        form = ProdutoForm()

    return render(request, 'produtos/form.html', {'form': form, 'nota': nota})

def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    nota = produto.nota  # Obtém a nota associada ao produto

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos', nota_id=nota.id)  # Redireciona corretamente
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'produtos/form.html', {'form': form, 'nota': nota})

def excluir_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == "POST":
        produto.delete()
        return redirect('lista_produtos', nota_id=produto.nota.id)  # Redireciona para a lista de produtos
    return render(request, 'produtos/confirmar_exclusao.html', {'produto': produto})

# Página inicial - Lista de Notas
def lista_notas(request):
    notas = Nota.objects.all()
    return render(request, 'produtos/notas.html', {'notas': notas})

# Adicionar Nota
def adicionar_nota(request):
    if request.method == "POST":
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotaForm()
    return render(request, 'produtos/form_nota.html', {'form': form})

# Editar Nota
def editar_nota(request, id):
    nota = get_object_or_404(Nota, id=id)
    if request.method == "POST":
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotaForm(instance=nota)
    return render(request, 'produtos/form_nota.html', {'form': form})

# Excluir Nota
def excluir_nota(request, id):
    nota = get_object_or_404(Nota, id=id)
    if request.method == "POST":
        nota.delete()
        return redirect('lista_notas')
    return render(request, 'produtos/confirmar_exclusao_nota.html', {'nota': nota})