N,M = map(int,input().split())
store = []

for _ in range(M):
  A,B = map(int,input().split())
  store.append((A,B))

store.sort(key=lambda x:x[0])
min_package = store[0][0]
store.sort(key=lambda x:x[1])
min_string = store [0][1]

package_only=(N//6+1)*min_package
string_only=N*min_string
package_string=(N//6)*min_package+(N%6)*min_string

print(min(package_only,string_only,package_string))