---
author: Milad Rafiei
layout: post
title: How to Implement Basic Security in Geoserver
date: 2024-06-05
categories:   
- Tutorials
---

[GeoSpatial Techno](https://www.youtube.com/@geospatialtechno) is a startup focused on geospatial information that is providing e-learning courses to enhance the knowledge of geospatial information users, students, and other startups. The main approach of this startup is providing quality, valid specialized training in the field of geospatial information.

( [YouTube](https://www.youtube.com/@geospatialtechno)
| [LinkedIn](https://www.linkedin.com/in/geospatialtechno)
| [Facebook](https://www.facebook.com/geospatialtechno)
| [X](https://twitter.com/geospatialtechn)
)

----

### How to Implement Basic Security in Geoserver
In this session, we want to discuss the Security section in GeoServer, Defining Users, Groups, and Roles, and Granting rights to created users. If you want to access the complete tutorial, simply click on the [link](https://youtu.be/KCTGZJ2Trvw).

[![](https://img.youtube.com/vi/KCTGZJ2Trvw/0.jpg)](https://www.youtube.com/watch?v=KCTGZJ2Trvw)

## Introduction
GeoServer has a robust security subsystem. Most of the security features are available through the Web Administration interface. In the Security panel, you can find links to set user properties and bind data to security rules. The basic idea is that you create users and roles, and then combine them with data rules to enable a specific set of access policies. You can also limit read and write access by role.

## Defining users, groups, and roles
Security in GeoServer is based on a role system where each role defines a specific set of functions. You can assign roles to users and groups; that is, assign functions to real people using your system. To ensure data security, you must identify who is accessing your layers and services.

To organize your real users, GeoServer provides you with the user, group, and role concepts. With the first two, you can insert real people into the GeoServer security subsystem, and with roles, you can grant rights to real users.

### User definition
In GeoServer, a user is someone entitled to use the system; it may be another software or a real person. When you add a user to the security system, GeoServer stores a username, uniquely identifying the user, a password, and a set of key/value pairs to store general information about it. You can disable a user at any time, preventing him from using the system.

### Group definition
A group in GeoServer is a collection of users. It consists of a list of usernames that are part of the group, along with a unique group name that identifies it. Since GeoServer may have a large number of users, assigning roles to each individual user can be challenging. Therefore, groups can be created to simplify the process, allowing roles to be assigned based on the group membership of users.

**Note**. Considering that there are no dependencies between users, groups, and roles. A group can be disabled, but note that this only removes the roles deriving from the disabled group and does not disable the users belonging to the group.

### Roles definition
GeoServer roles are associated with performing certain tasks or accessing particular resources. Roles are assigned to users and groups, authorizing them to perform the actions associated with the role. 

## Creating users and groups
To fully understand how security works in GeoServer, we will use a typical scenario. We want to restrict access to this data to only the organization's members. Inside the organization, there are a few people editing data to create new data sets or to update existing ones, and many more members who need to read data to compose maps. There is also a need for an administrator to keep it all working. Lastly, we need to consider that our GeoServer site also contains data that should remain freely available. We will now create the security organization from an unsecured GeoServer as follows:
- In the Security section of the left pane, click the **Users, Groups, and Roles** link. This link shows you the User Group Services configured. You will find the default service shipped with GeoServer. Click on the **Name** to edit it.
- Select the **Groups** tab, then click on **Add a new group**.
- Enter `group_readers` as a group name and leave the group Enabled. Do not assign any role to the new group as we will create specific roles later. Press the **Save** button.
- Repeat the previous step to create the `group_editors` and `group_admins` groups. Your list should now show the three groups.
- Now switch to the **Users** tab. Obviously, it lists the only existing user, that is, admin, as shown in the screen.
- Click on the **Add new user** link, and add `user_admin` with a password of your choice, as Data Administrator.
- Add "user_admin" to the "group_admins", then press the **Save** button.
- Repeat the previous step to create a user, `user_editor` as a member of the "group_editors" group, and `user_reader` as a "group_readers" group member. Your list now shows the three users.

We just created three users for the three groups and this may seem overkill to you. Consider them as templates for real users. In the real world, we do not want to have too many administrators; we will probably need several "user_readers" and "user_editors" processing the data. Now, we need to define what they can do on GeoServer.

## Defining roles
A user or a group without any role assigned is useless. Now it is time to create roles and assign them to our users. Please refer to the following points:
- From the **User, Groups, and Roles** section, select the **Roles** tab. You will find that two roles already exist. They are the administrative roles assigned to the admin account, and they grant access to all GeoServer configurations. Click on the **Edit** link
- Switch to the **Roles** tab, then click on **Add new role**.
- Enter `role_reader` as a new role name. We do not need a Parent role. A child role inherits all the rights from the Parent role, making it useful when you want to extend a basic role with more rights. Indeed, we will do this in the next step. 
- Press the **Save** button and then repeat the previous step to create the `role_editor` role. This time, select "role_reader" as the Parent role.
- Press the **Save** button and then repeat the previous step to create the `role_admin` role. This time, select "role_editor" as the Parent role.
- The final step is to associate a role to users or groups. Select the **User, Groups, and Roles** page from the left pane, then select the **Groups** list and click on the "group_readers" group to edit it. Add the "role_reader" role to the group and save it.
- Now click on the "group_editors" group and associate it with the role_editor role.
- Finally, associate the "group_admins" group to the "role_admin" role.

By defining roles and associating them to the users, we completed the definition of our organization. Now, we need to explore how data is bound to roles and users.

## Accessing data and services
GeoServer supports access control at both the service level and at the per-layer or per-workspace level, allowing for restriction of service operations to authenticate users with specific roles. This helps in ensuring data security and controlling access to different layers or workspaces within the server. When working with layers, you can define rules that specify what a role can do on any specific layer.

The operations controlled are the view, write, and admin access. When granting read access on a layer, you enable a user to add it on a map; while granting write access you enable the user to update, create, and delete features contained in the layer. The admin access level enables the user to update the layer’s configuration.

## Layer Security
We want to protect the dataset contained in the `test` workspace from unauthorized access while leaving the remaining layers freely available to all users. In this section, we will associate layers and roles:
- Navigate to the Data > Security page. The rules list shows the two shipped with the default GeoServer configuration.
The `*.*.r` rule is associated with the `*` roles. 
This means that "any user", including the anonymous one, can access "any layer" from "any workspace" configured on GeoServer. The general format of the rules is: **workspace.layer.accessMode**.
- Now click on the Add new rule link. In the rule editing page, select `test` as the Workspace and leave "*" as a Layer. 
Since we want to protect all layers in this workspace, the **Access** mode should be **Read**. Select the "role_reader" role and move it to the right list by clicking on the arrow. Press the **Save** button to create the reading rule.
- Repeat the previous step to create a writing rule. Select **Write** as the access mode and "role_editor" as the role.
- Repeat the previous step, then create the administration rule. In other words, select **Admin** as the Access mode and "role_admin" as the Role. 
- Press the Save button, on the rule list page, and then log off from the GeoServer web interface. If you try to access the layer preview anonymously, you won't see any layers from the `test` workspace while all the others are still listed.
- Now, log on as "user_reader", with the password you assigned to him. Going back to the layer preview, you should see the `test` layers listed. Try the **Open Layers** preview page for the `river` layer. It works and you can use the data to compose maps.
- However, "user_reader" can't edit the styles associated with the layer or any other property. He would need admin rights granted for it; can you guess who the proper user will be?
- Log on to GeoServer as "user_admin". Now, the left pane is richer than it was when you were "user_reader", but with fewer features than those visible to the GeoServer's default admin role. Click on the **Layer** link; you will see only the layers belonging to the `test` workspace.
- If you go on Layer preview and select the `rivers` layer again, can you see the map? Of course, you can. Because of roles inheritance, which you set when creating the roles. So, "role_admin" inherits all the rights from "role_editor", and hence from "role_reader".

----

In this session, we took a brief journey through GeoServer security. we discussed the **Security** section, **Defining Users, Groups, and Roles, and Granting rights to created users** in GeoServer. If you want to access the complete tutorial, simply click on the [link](https://youtu.be/KCTGZJ2Trvw).

[![](https://img.youtube.com/vi/KCTGZJ2Trvw/0.jpg)](https://www.youtube.com/watch?v=KCTGZJ2Trvw)