import re
from doublyLinkedListIterator import DoublyLinkedListIterator
from singlyLinkedListIterator import SinglyLinkedListIterator

class main:
    def printList(list: SinglyLinkedListIterator):
        if list.size == 0:
            return False

        list.first_Node()
        
        while list.iterator:
            print(f'[{list.iterator.data}, {list.iterator.listaDE}]')
            list.nextNode()


    def printListData(list: SinglyLinkedListIterator):
        if list.size == 0:
            return False

        list.first_Node()
        
        while list.iterator:
            print(list.iterator.data)
            list.nextNode()

    def printListListaDE(list: SinglyLinkedListIterator):
        if list.size == 0:
            return False

        list.first_Node()
        
        while list.iterator:
            print(list.iterator.listaDE)
            list.nextNode()
    
    def getHighways():
        """Função responsável por receber e ler os dados do arquivo entries.txt no diretório

        Returns:
            _SinglyLinkedListIterator_: Lista simplesmente encadeada contendo o nome da rodovia e uma lista
            duplamente encadeada com as cidades onde essa rodovia passa.
        """
        highwaysList = SinglyLinkedListIterator()
        citiesList = DoublyLinkedListIterator()
        
        # LEITURA DO ARQUIVO QUE CONTÉM AS RODOVIAS E AS CIDADES ( neste caso, "./entries.txt")
        entries = open("entries.txt")
        lines = entries.readlines()

        # DEFINO O NÓ INICIAL NAS MINHAS LISTAS DE ROVIAS E CIDADES.
        highwaysList.first_Node()
        citiesList.first_Node()

        for line in lines:
            # AQUI EU UTILIZEI DO MÉTODO findall() e REGEX PARA PARA RECEBER A RODOVIA. 
            highway = re.findall(r"[A-Z]{2}-\d{3}", line)
            # SEMELHANTEMENTE FIZ PARA RECEBER AS CIDADES
            cities = re.findall(r'"([^"]+)"', line)

            # PARA CADA CIDADE ENCONTRADA, ADICIONE UM NÓ NA LISTA DUPLAMENTE ENCADEADA
            for city in cities:
                citiesList.addNode(city)

            # POR FIM, ADICIONE A RODOVIA, NO PRIMEIRO ARGUMENTO DA FUNÇÃO addNode() E A
            # LISTA DUPLAMENTE ENCADEADA NO SEGUNDO.
            highwaysList.addNode(highway[0], cities)
        return highwaysList


    def cityHighways(cityName: str, highwaysList: SinglyLinkedListIterator):
        """Retorna as rodovias que passam pela cidade recebida em cityName.

        Args:
            cityName (str): Nome da cidade a qual será comparada 
            se uma rodovia passa ou não por ela.
            highwaysList (SinglyLinkedListIterator): Lista simplesmente encadeada
            que contém o nome da rodovia, e uma lista duplamente encadeada contendo 
            o nome das cidades as quais essa rodovia passa.

        Returns:
            SinglyLinkedListIterator: Rodovias que passam pela cidade recebida no argumento
            cityName.
        """
        # DEFINO A LISTA QUE IREI RETORNAR COM AS RODOVIAS E DEFINO O PRIMEIRO NÓ
        # DA highwaysList RECEBIDA COMO ARGUMENTO.
        highways = SinglyLinkedListIterator()
        highwaysList.first_Node()
    
        # ENQUANTO EXISTIREM NÓS NA LISTA RECEBIDA, FAÇA:    
        while highwaysList.iterator:
            # PARA CADA CIDADE ENCONTRADA DENTRO DA LISTA DUPLAMENTE ENCADEADA DO NÓ ATUAL, FAÇA:
            for city in highwaysList.iterator.listaDE:
                # SE O NOME DA CIDADE ENCONTRADO NA LISTA DUPLAMENTE ENCADEADA FOR IGUAL A CIDADE
                # PASSADA NO PARÂMETRO cityName ADICIONE À LISTA QUE IREI RETORNAR O NOME DA RODOVIA.
                if city == cityName:
                    highways.addNode(highwaysList.iterator.data, None)
            # ITERO PARA O PRÓXIMO NÓ.
            highwaysList.nextNode()

        return highways
    
    if __name__ == "__main__":
        
        highways = getHighways()

        result = cityHighways("Joinville", highways)
        
        printListData(result)