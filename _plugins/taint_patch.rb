# _plugins/taint_patch.rb
class Object
  unless method_defined?(:tainted?)
    def tainted?
      false
    end
  end
end

