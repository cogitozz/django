from django.shortcuts import render
from django.http import HttpResponseRedirect  # 用户提交主题后我们将使用这个类将用户重定向到网页topics
from django.urls import reverse # 函数reverse() 根据指定的URL模型确定URL，这意味着Django 将在页面被请求时生成URL。
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by()
    # topic = Topic.objects.filter(owner=request.user).order_by()
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """显示单个主题及其所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """用户添加新主题"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)  # 使用用户输入的数据（它们存储在request.POST 中）创建一个TopicForm 实例
        if form.is_valid():     # 。函数is_valid() 核实用户填写了所有必不可少的字段（表单字段默认都是必不可少的），且输入的数据与要求的字段类型一致
            form.save()     # 将提交的信息保存到数据库
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}        #  通过上下文字典将表单发送给模板
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """在特定的主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 未提交数据，创建一个空表单
        form = EntryForm()
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)     # 让Django创建一个新的条目对象，并将其存储到new_entry 中，但不将它保存到数据库中。
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))    # 我们将用户重定向到显示相关主题的页面。
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """编辑既有的条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)    # 这个实参让Django创建一个表单，并使用既有条目对象中的信息填充它。用户将看到既有的数据，并能够编辑它们。
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)     # Django根据既有条目对象创建一个表单实例，并根据request.POST 中的相关数据对其进行修改。
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
