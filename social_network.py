class Person:
    """
    A class representing a person in a social network.

    Attributes:
        name (str): The name of the person.
        friends (list): A list of Person instances this person is connected to.
    """

    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if isinstance(friend, Person) and friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    """
    A class representing a social network using an adjacency list.

    Attributes:
        people (dict): A dictionary mapping names to Person instances.
    """

    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name not in self.people:
            self.people[name] = Person(name)
        else:
            print(f"{name} already exists in the network.")

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return
        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]
            print(f"{name} is friends with: {', '.join(friend_names)}")



if __name__ == "__main__":
    network = SocialNetwork()

    
    network.add_person("Alex")
    network.add_person("Jordan")
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")
    network.add_person("Alex")  

   
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    
    network.add_friendship("Jordan", "Jamie")  

    
    network.print_network()


# A graph is the right structure to represent a social network because it mirrors the way relationships work in real life. people (nodes) are connected to other people (edges), 
# and those connections can be many-to-many and bidirectional. Unlike hierarchical structures like trees, which enforce parent-child relationships, graphs allow for flexible, non-linear connections.
#  This is essential in a social network where any person can be friends with any number of others, and those friendships can form complex webs of interaction.
#  Graphs also support efficient algorithms for exploring relationships, such as finding mutual friends, shortest paths between people, or detecting communities.
#  For example, if you want to suggest new friends based on shared connections, a graph makes it easy to traverse and analyze those links.



#A list or tree wouldn’t work as well for representing a social network because they lack the flexibility to model complexes.
#  A list is a linear structure that stores elements sequentially. While you could store all people in a list, it doesn’t capture how they’re connected. 
# You’d need a separate structure to track friendships, which quickly becomes messy and inefficient. Lists don’t support direct relationships between elements unless you manually build and maintain those connections.
#  A tree is even more restrictive. It enforces a hierarchical structure where each node has one parent and possibly multiple children, but no cycles.
#  That’s a poor fit for social networks, where people can be connected in loops, share mutual friends, and form dense clusters. 


# several performance and structural trade-offs become apparent, especially when adding friends and printing the network. When it comes to adding friends, the network uses an adjacency list structure (a dictionary of Person objects), 
# which makes adding a person efficient, constant time insertion if the name is unique. However, adding a friendship requires checking that both people exist and then updating each person's friends list.
#  Now when it comes to printing the network Printing the network involves iterating through every person and then through each of their friends to display names. 
# This is a nested loop, one over the people, and one over each person’s friends. While this is manageable for small networks, it scales poorly with size. 

