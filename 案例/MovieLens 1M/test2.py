import pandas as pd
# 假设有一个普通的 DataFrame
df_flat = pd.DataFrame({
    'Group': ['Group A', 'Group A', 'Group B', 'Group B'],
    'Gender': ['Male', 'Female', 'Male', 'Female'],
    'Score': [88, 92, 85, 89]
})

print("\n--- 原始的扁平 DataFrame ---")
print(df_flat)

# 使用 set_index() 创建多级索引
df_multi = df_flat.set_index(['Group', 'Gender'])

print("\n--- 使用 set_index() 创建的多级索引 DataFrame ---")
print(df_multi)