# ingredients = []
#
#
# # def still_have_ingreditents():
# #     for m_packages in ingredients:
# #         if m_packages != []:
# #             return True
# #     return False
#
#
# t = int(raw_input())  # read a line with a single integer
# for i in xrange(1, t + 1):
#     n, p = [int(s) for s in raw_input().split(" ")]
#     ratatouille_serving = [int(s) for s in raw_input().split(" ")]
#
#     for _ in xrange(n):
#         ingredients.append([int(s) for s in raw_input().split(" ")])
#
#     num_kits = 0
#
#     possible = True
#     while possible:
#         ingredient_i = 0
#
#         kit = []
#         while ingredient_i < n:
#             number_of_servings = 1
#             package_i = 0
#             packages = ingredients[ingredient_i]
#             possible = False
#             while package_i < len(packages):
#                 package = packages[package_i]
#                 while package > number_of_servings*ratatouille_serving[ingredient_i] * 1.1:
#                     number_of_servings += 1
#                 if number_of_servings*ratatouille_serving[ingredient_i] * 0.9 <= package <= number_of_servings*ratatouille_serving[ingredient_i] * 1.1:
#                     kit.append(ingredients[ingredient_i].pop(package_i))
#                     possible = True
#                     for l in xrange(len(kit)):
#                         e = kit[l]
#                         if e > number_of_servings*ratatouille_serving[l] * 1.1 or e < number_of_servings*ratatouille_serving[l] * 0.9 :
#                             possible = False
#                             break
#                     break
#                 number_of_servings = 1
#                   package_i += 1
#             if not possible:
#                 break
#             ingredient_i += 1
#         if possible:
#             num_kits += 1
#         else:
#             break
#
#     print "Case #{}: {}".format(i, num_kits)
