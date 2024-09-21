import pytest
import app

@pytest.mark.parametrize(
        'user_doc_number,expected',
        (
            ('2207 876234', True),
            ('11-2', True),
            ('10006', True),
            ('5455 028765', False),
            ('1', False),
            (1,False),
            ('\n', False),
            (False, False)

        )
)
def test_check_document_existance(user_doc_number, expected):
    assert app.check_document_existance(user_doc_number) == expected

@pytest.mark.parametrize(
    'number,expected',
    (
        ('2207 876234',"Василий Гупкин"),
        ('11-2',"Геннадий Покемонов"),
        ('10006',"Аристарх Павлов"),
        ('5455 028765', None),
        ('1', None),
        (1,None),
        ('\n', None)
    )

)
def test_get_doc_owner_name(number, expected):
    assert app.get_doc_owner_name(number) == expected

def test_get_all_doc_owners_names():
    expected = set(("Василий Гупкин","Геннадий Покемонов","Аристарх Павлов"))
    assert app.get_all_doc_owners_names() == expected

@pytest.mark.parametrize(
    'doc_number, expected',
    (
        ('2207 876234', '1'),
        ('10006','2'),
        ('', None)
    )
)
def test_get_doc_shelf(doc_number, expected):
    result = app.get_doc_shelf(doc_number)
    assert result == expected

def test_move_doc_to_shelf():
    doc_num = '11-2'
    app.move_doc_to_shelf(doc_num, '3')
    assert not doc_num in app.directories['1'] and doc_num in app.directories['3']

@pytest.mark.parametrize(
        'doc_number,shelf,expected',
        (
            ('2207 876234','1', True),
            ('10006','2',True)
            #(10006, '2',False)
        )
)
def test_remove_doc_from_shelf(doc_number, shelf,expected):
    app.remove_doc_from_shelf(doc_number)
    if type(doc_number) == int:
        doc_number = str(doc_number)
    result = not doc_number in app.directories[shelf]
    assert result == expected 

@pytest.mark.parametrize(
        'doc_number,expected',
        (
            ('2207 876234', True),
            ('1', False)
        )
)
def test_delete_doc(doc_number, expected):
    len_before = len(app.documents)
    app.delete_doc(doc_number)
    assert (len_before == len(app.documents) + 1) == expected

def test_add_new_shelf():
    len_before = len(app.directories)
    app.add_new_shelf('4')
    assert len_before + 1 == len(app.directories)

def test_append_doc_to_shelf():
    len_before = len(app.directories['1'])
    app.append_doc_to_shelf(1,'1')
    assert len(app.directories['1']) == len_before + 1

def test_add_new_doc():
    doc_num = '1'
    doc_type = 'test'
    doc_owner = 'Test Test Test'
    doc_shelf = '5'
    app.add_new_doc(doc_num, doc_type, doc_owner, doc_shelf)
    assert '5' in app.directories and doc_num in app.directories['5'] and {'type':doc_type, 'number': doc_num, 'name':doc_owner} in app.documents












